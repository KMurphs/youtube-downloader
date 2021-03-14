from datetime import datetime
from enum import Enum

class Status(Enum):
    NOT_DOWNLOADED = 0

class Video():
  
  def __init__(self, link: str = "", title: str = "", length: str = "", stream_tag_of_interest: int = 0, thumbnail: str = "", author = "", keywords = ""):
    self.link: str = link
    self.title: str = title
    self.length: str = length
    self.stream_tag_of_interest: int = stream_tag_of_interest
    self.thumbnail_path: str = thumbnail
    self.author: str = author
    self.keywords: str = keywords
    
    self.addedAt: int = datetime.timestamp(datetime.now())
    self.strAddedAt: str = self.timestampToString(self.addedAt)
    
    self.completedAt: int = 0
    self.strCompletedAt: str = ""

    self.status: Status = Status.NOT_DOWNLOADED



  def timestampToString(self, timestamp):
    try:
      strTimestamp = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
    except Exception as e:
      strTimestamp = ""
      pass
    return strTimestamp

  def fromDict(self, myObject: dict):
    for key in myObject.keys():
      if key in self.__dict__.keys():
        self.__dict__[key] = myObject[key]
    self.strCompletedAt = self.timestampToString(self.completedAt)
    return self

  def toDict(self):
    return vars(self)