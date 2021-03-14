from pytube import YouTube
import logging
import re
import time
from datetime import datetime

from utils.app_types import YoutubeDownloadItem

RETRY_PERIOD = 30
RETRY_AMOUNT = 3


def fetch_parameters(iterator, downloadsDB, use_prompts):
  """Will prompt user for youtube video links, and extract information needed to perform the download at a later stage.
  These parameters will then be saved to the file 'tasks_file'

  Args:
      tasks_file (str): File that contains information about all the youtube downloads that will be executed later on
  """

  

  # Prompt for new link
  input_link = None
  for input_link in iterator:

    # Should we be stopping?
    if(input_link == ""): 
      logging.info("Stopping...")
      continue
    

    # Do we have that input link in the db?
    results: List[YoutubeDownloadItem] = list(filter(lambda x: x.link == input_link, downloadsDB))
    if len(results) > 0 and results[0].stream_tag_of_interest > 0: 
      logging.info(f"Link '{input_link}' has already been successfully processed")  
      continue


    # Gather parameters with retries
    for _ in range(RETRY_AMOUNT):


      try:
        logging.info(f"Processing Link: {input_link}") 
        completed = False

        # Query remote video
        title, length, stream_tag_of_interest, author, keywords = fetch_parameter(video_link = input_link, use_prompt = use_prompts)
        
        # Save parameters with object to be downloaded
        item_to_download = YoutubeDownloadItem(link = input_link, title = title, length = length, stream_tag_of_interest = stream_tag_of_interest, addedAt = datetime.timestamp(datetime.now()), author = author)
        downloadsDB.append(item_to_download)
        completed = True

        # Summarize Processing operations for user feedback
        logging.info(f"Link '{input_link}' was successfully processed")  
        logging.info(f"Video '{item_to_download.title}' ({item_to_download.length} - Stream {item_to_download.stream_tag_of_interest}) is configured for download\n")
        break

      # Retry on error
      except Exception as e: 
        logging.warning(f"Link '{input_link}' could not be processed. Re-attempting in {RETRY_PERIOD}sec")  
        time.sleep(RETRY_PERIOD)
        pass
    
    # Indicate our inability to contact remote video at this time
    if not completed: logging.error(f"Permanent Error trying to process '{input_link}'") 
  
  return downloadsDB


def fetch_parameter(video_link, use_prompt = True):
  """Builds an object gathering all the parameters needed to download the video at a later stage

  Args:
      video_link (str): A http(s) link to the Youtube Video to be downloaded
      use_prompt (str): Indicates whether to ask the user which stream to download from

  Returns:
      [title (str), length (str), stream_number (int)]: title, length, stream_number of the video to be downloaded
  """
  number_pattern: str = "[0-9]+"


  # Connect to target object
  yt = YouTube(video_link)

  # Extract progressive streams. 
  # Progressive streams have max resolution of 720px, 
  # compared to Dash Streams the alternative 
  # (higher resolution, but only video codec without sound)
  # We would have to be clever and mix the video and sound codecs using some other tools
  streams = str(yt.streams.filter(progressive=True))
  streams_list: List[str] = streams[1:-1].split(", ")
  itags: List[int] = []



  # Allow user to choose which stream (identified by its itag) to download 
  for stream_item in streams_list:
    st_parts = stream_item.split(" ")

    # Get the interesting parts
    itag = st_parts[1]
    resolution = st_parts[3]

    # Strip the itag from the surrounding text
    itag_index = int(re.search(number_pattern, itag).group())
    itags.append(itag_index)

    if use_prompt: print(f"{itag_index}) {itag} and {resolution}")



  # Prompt user to choose for a specific itag to download
  itag_index_of_interest = int(input("Enter itag number of stream to download: ")) if use_prompt else itags[0]
  print("\n")
  if not itag_index_of_interest in itags:
    itag_index_of_interest = itags[0]


  return [ yt.title, f"{yt.length}sec", itag_index_of_interest, yt.author, yt.keywords ]


