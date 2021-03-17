from datetime import datetime
import hashlib
import os
from typing import Dict

def url_to_filename(url, extension = "png"): return f"{hash_string(url)}-{datetime.now().strftime('%Y%m%d%H%M%S-%f')}.{extension}"
def dict_from_class(obj): return dict((name, getattr(obj, name)) for name in dir(obj) if not name.startswith('__')) 
def dict_from_class_props(cls): 
  import inspect
  pr = {}
  for name in dir(cls):
    value = getattr(cls, name)
    if not name.startswith('__') and not inspect.ismethod(value):
      pr[name] = value
  return pr

def hash_string(in_str): return hashlib.sha256(in_str.encode()).hexdigest()

def build_absolute_path(filename, relative_path_parts = ["..", "thumbnails"]): return os.path.realpath(os.path.join(os.getcwd(), *relative_path_parts, filename))


def set_key_on_dict(key: str, src: Dict, dst: Dict): return { key: src.get(key, dst.get(key, None)) }