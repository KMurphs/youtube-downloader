from datetime import datetime
from enum import Enum
import urllib.request
from pytube import YouTube
import logging

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


