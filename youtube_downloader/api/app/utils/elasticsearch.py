import logging
from elasticsearch import Elasticsearch

def debug(fn):
    def decorated_fn(*args, **kwargs):
        res = fn(*args, **kwargs)
        logging.debug(res)
        return res
    return decorated_fn

def with_logging(level=logging.DEBUG, msg = None):
    def _with_logging(fn):
        def decorated_fn(*args, **kwargs):
            res = fn(*args, **kwargs)
            print("\n***************", f"\n{msg}", "\nExecuting with Args: ", *args, **kwargs)
            logging.log(level, res)
            return res
        return decorated_fn
    return _with_logging



index = "videos"
__es = None
def get_connection():
    global __es
    if __es is None: __es = Elasticsearch()
    if not __es.indices.exists(index): __es.indices.create(index)
    return __es




def get_video_by_id(id): return get_connection().get(index, id)
def get_videos(url): return get_connection().search(index=index, body={"query": {"match_all": {}}})

# def get_video_by_url(url): return get_connection().search(index=index, body={"query": {"match": {"watch_url":url}}})
# def get_video_by_url(url): return get_connection().search(index=index, body={"query": {"bool": {"must": [ {"match": {"watch_url":url}}]}}})

@with_logging(level=logging.DEBUG, msg="This value")
def get_video_from_props(field, value): return get_connection().search(index=index, body={"query": {"term": {field: value}}})

# def get_video_by_url(url): return get_connection().search(index=index, body={"query": {"wildcard": {"watch_url.keyword": f"*{url.split('/')[-1]}"}}})
def create_video(video): return get_connection().index(index, body=video)
def update_video(id, video): return get_connection().index(index, id=id, body=video)
