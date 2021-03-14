import logging
import os
import hashlib
import urllib.request
from pytube import YouTube
from datetime import datetime
from typing import Dict
from functools import reduce
from utils.elasticsearch import get_video_from_props

class RemoteVideo:
  def __init__(self, link):
    self.link = link

  def connect(self): 
    try:
      return YouTube(self.link)
    except Exception as e:
      return None



class RemoteImage:
  def __init__(self, link):
    self.link = link

  def download(self, save_name): 
    try:
      urllib.request.urlretrieve(self.link, save_name)
      return save_name
    except Exception as e:
      logging.error(e)
      return None


def dict_from_class(obj): return dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('__')) 
def dict_from_class_props(cls): 
  import inspect
  pr = {}
  for name in dir(cls):
    value = getattr(cls, name)
    if not name.startswith('__') and not inspect.ismethod(value):
      pr[name] = value
  return pr




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


def hash_string(in_str): return hashlib.sha256(in_str.encode()).hexdigest()
def build_thumbnail_name(thumbnail_url): return f"{hash_string(thumbnail_url)}-{datetime.now().strftime('%Y%m%d%H%M%S-%f')}.png"
def build_absolute_path(filename, relative_path_parts = ["..", "thumbnails"]): return os.path.realpath(os.path.join(os.getcwd(), *relative_path_parts, filename))


def __get_video_streams(src: Dict, resolution = '720p'): return [(resolution, stream.itag) for stream in src['streams'].filter(progressive=True).filter(res=resolution)] 
def get_video_streams(src: Dict):
  streams = __get_video_streams(src, f"{src.get('user_resolution')}p") + __get_video_streams(src)
  return dict(streams + [("default", streams[0][1])])





def set_key_on_dict(key: str, src: Dict, dst: Dict): return { key: src.get(key, dst.get(key, None)) }
def build_video_metadata(src, dst = {}, is_new = False):
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
    lambda src, dst, key="video_path": set_key_on_dict(key, src, dst),
    lambda src, dst, key="added_at": set_key_on_dict(key, src, dst),
    lambda src, dst, key="added_at_str": set_key_on_dict(key, src, dst),
    lambda src, dst, key="completed_at": set_key_on_dict(key, src, dst),
    lambda src, dst, key="completed_at_str": set_key_on_dict(key, src, dst),
  ]

  return reduce(lambda acc, fn: acc | fn(src, dst), metadata_fns, dict())

def decorate_remote_obj(src: Dict, video: Dict, is_new=False):

  src = src | video

  src['uri'] = get_uri(src['watch_url']) 
  src['streams'] = get_video_streams(src)
  src['thumbnail_filename'] = build_thumbnail_name(src['watch_url'])
  src['thumbnail_filepath'] = build_absolute_path(src['thumbnail_filename'])

  if is_new:
    ts = datetime.timestamp(datetime.now())
    ts_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")
    src['added_at'] = ts
    src['added_at_str'] = ts_str
    src['completed_at'] = None
    src['completed_at_str'] = None
    src['status'] = 0
  return src

def process_video(video: Dict, is_new=False):
  
  # Attempt connection to remote video
  yt = RemoteVideo(video.get("url")).connect()
  if yt is None: raise Exception(400, f"Could not process link '{video.get('url')}'")

  # Transform Class to dict
  src = dict_from_class(yt)
  src = decorate_remote_obj(src, video, is_new)

  # Attempt downloading the thumbnail
  tb = RemoteImage(src['thumbnail_url']).download(src['thumbnail_path'])

  # Build and validate metadata
  metadata = build_video_metadata(src)
  if metadata["title"] is None: raise Exception(400, f"Could not process link '{video.get('url')}'")
  return metadata
  

def video_from_user_data(obj: Dict): 
  if not obj.get("url") or ("youtube" not in obj.get("url", "")): raise Exception(400, "Invalid video url was provided")
  return {
    "user_resolution": obj.get("resolution", None),
    "url": obj.get("url", None),
    "tags": obj.get("tags", [])
  }

def get_video_by_url(url): return get_video_from_props('uri_hash', hash_string(get_uri(url)))