from datetime import datetime
import json
import logging
import os
from typing import Dict
from functools import reduce

from pytube import YouTube
from utils.types import RemoteImage, RemoteVideo
import utils.elasticsearch_manager as em
from utils.utils import build_absolute_path, dict_from_class, hash_string, set_key_on_dict, str_to_filename, url_to_filename








def process_video(video: Dict, is_new=False):
  
  logging.debug(f"Attempt connection to remote video '{video.get('url')}'")
  yt = RemoteVideo(video.get("url")).connect()
  if yt is None: raise Exception(400, f"Could not process link '{video.get('url')}'")

  # Transform Class to dict
  src = dict_from_class(yt)
  src = decorate_remote_obj(src, video, is_new)
  logging.debug(f"Decorated remote object for '{video.get('url')}' - keys: {json.dumps(list(src.keys()))}")

  logging.debug(f"Attempt downloading to thumbnail for '{video.get('url')}'")
  tb = RemoteImage(src['thumbnail_url']).download(src['thumbnail_filepath'])

  logging.debug(f"Build and validate metadata for '{video.get('url')}'")
  metadata = build_video_metadata(src)
  if metadata["title"] is None: raise Exception(400, f"Could not process link '{video.get('url')}'")
  return metadata
  



def download_videos():
  logging.info(f"Starting download videos routine")
  it = em.get_results_iterator(query = { "bool": {"filter": [{ "term":  { "status": "0" } }] }})
  for doc in it:
    
    id = doc.get('_id')
    video = doc.get('_source')
    url = video.get('watch_url')
    streams = video.get('streams')
    video_path = video.get('video_filepath')

    logging.info(f"Processing video '{id}': {url}")
    yt = YouTube(url)
    ys = get_download_stream(yt, streams)
    logging.info(f"Downloading stream '{ys[1]}' as {video_path}")
    try: 
      ys[0].download(os.path.split(video_path)[0])
      video['status'] = 1
      ts = datetime.timestamp(datetime.now())
      ts_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
      video['completed_at'] = int(ts*1000)
      video['completed_at_str'] = ts_str
      em.update_video(id, video)
      logging.info(f"Downloaded successfully: {ts_str}")
    except Exception as e: pass



def get_video_by_url(url): return to_VideoRecord(em.get_video_from_props('uri_hash', hash_string(get_uri(url))))
def get_video_by_id(id): return to_VideoRecord(em.get_video_by_id(id))
def update_video(id, video): return em.update_video(id, video)
def create_video(video): return em.create_video(video)
def get_name_from_id(id): return em.get_video_by_id(id)["_source"]['video_filename']
def get_path_from_id(id): return em.get_video_by_id(id)["_source"]['video_filepath']
def get_zipfile_details(url_root, filename = "bundle"): 
  
  name = str_to_filename(filename, "zip")
  path = build_absolute_path(name, relative_path_parts=["..", "bundles"])
  url = f"{url_root}bundles/{name}"
  return (name, path, url)

def get_search_url(args = None, prettify = True): return em.get_search_url(args, prettify)



def get_uri(video_link): 
  """The same video can have multiple urls pointing to it. e.g 
  - youtube.com/... and www.youtube.com/..., or 
  - /v=video-id and /v=video-id&index=2

  This can lead to subtle bugs.
  This function will attempt to extract the unique true constant video id from the url.
  
  Args:
      video_link (string): url of some video
  Returns:
      string: part of the url that actually identifies the video
  """
  return video_link.split('/')[-1].split('&')[0]





def to_VideoRecord(es_results):
  logging.debug('Transforming ' + json.dumps(es_results) + ' to video record')
  res = {"__es": es_results} | {"total": len(es_results["hits"]["hits"])} | { "video": {} } | { "videos": [] }
  if type(es_results) is not dict or "hits" not in es_results.keys() or "total" not in es_results["hits"].keys(): 
    return res | {"message": "Could not query elasticsearch"}
  if res["total"] == 0: return res
  if res["total"] == 1: 
    return res | { "videos": [] } | {"video":  [{"id": r.get("_id")} | r.get("_source") for r in es_results["hits"]["hits"]][0]} 
  return   res | { "video" : {} } | {"videos": [{"id": r.get("_id")} | r.get("_source") for r in es_results["hits"]["hits"]]   }



def video_from_user_data(obj: Dict): 
  if not obj.get("url") or ("youtube" not in obj.get("url", "")): raise Exception(400, "Invalid video url was provided")
  return {
    "user_resolution": obj.get("resolution", None),
    "url": obj.get("url", None),
    "tags": obj.get("tags", [])
  }


def decorate_remote_obj(src: Dict, video: Dict, is_new=False):

  src = src | video

  src['uri'] = get_uri(src['watch_url']) 
  src['streams'] = get_video_streams(src)
  src['thumbnail_filename'] = url_to_filename(src['watch_url'], "png")
  src['thumbnail_filepath'] = build_absolute_path(src['thumbnail_filename'], relative_path_parts=["..", "thumbnails"])
  src['video_filename'] = f"{src['title']}.mp4"
  src['video_filepath'] = build_absolute_path(src['video_filename'], relative_path_parts=["..", "videos"])
  
  if is_new:
    ts = datetime.timestamp(datetime.now())
    ts_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    src['added_at'] = int(ts*1000)
    src['added_at_str'] = ts_str
    src['completed_at'] = None
    src['completed_at_str'] = None
    src['status'] = 0
  return src


def build_video_metadata(src, dst = {}):
  metadata_fns = [
    lambda src, dst, key="title": set_key_on_dict(key, src, dst),
    lambda src, dst, key="author": set_key_on_dict(key, src, dst),
    lambda src, dst, key="length": set_key_on_dict(key, src, dst),
    lambda src, dst, key="keywords": set_key_on_dict(key, src, dst),
    lambda src, dst, key="tags": set_key_on_dict(key, src, dst),
    lambda src, dst, key="uri": set_key_on_dict(key, src, dst),
    lambda src, dst, key="uri_hash": set_key_on_dict(key, src, {key: hash_string(src['uri'])}),
    lambda src, dst, key="watch_url": set_key_on_dict(key, src, dst),
    lambda src, dst, key="thumbnail_url": set_key_on_dict(key, src, dst),
    lambda src, dst, key="thumbnail_filepath": set_key_on_dict(key, src, dst),
    lambda src, dst, key="thumbnail_filename": set_key_on_dict(key, src, dst),
    lambda src, dst, key="streams": set_key_on_dict(key, src, dst),
    lambda src, dst, key="status": set_key_on_dict(key, src, dst),
    lambda src, dst, key="video_filename": set_key_on_dict(key, src, dst),
    lambda src, dst, key="video_filepath": set_key_on_dict(key, src, dst),
    lambda src, dst, key="added_at": set_key_on_dict(key, src, dst),
    lambda src, dst, key="added_at_str": set_key_on_dict(key, src, dst),
    lambda src, dst, key="completed_at": set_key_on_dict(key, src, dst),
    lambda src, dst, key="completed_at_str": set_key_on_dict(key, src, dst),
  ]

  return reduce(lambda acc, fn: acc | fn(src, dst), metadata_fns, dict())



def __get_video_streams(src: Dict, resolution = '720p'): return [(resolution, stream.itag) for stream in src['streams'].filter(progressive=True).filter(res=resolution)] 
def get_video_streams(src: Dict):
  streams = __get_video_streams(src, f"{src.get('user_resolution')}p") + __get_video_streams(src)
  return dict(streams + [("default", streams[0][1])])
def get_download_stream(remote_video: YouTube, streams: Dict): 
  for stream in ['default'] + list(streams.keys()):
    try: return (remote_video.streams.get_by_itag(streams.get(stream)), streams.get(stream))
    except Exception as e: pass
  return (None, None)