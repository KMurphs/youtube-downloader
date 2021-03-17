# from pytube import YouTube
# import logging
# import time
# from datetime import datetime

# from utils.app_types import YoutubeDownloadItem
import sys
print(sys.path[0])
import utils.elasticsearch_manager as em

# RETRY_PERIOD = 30
# RETRY_AMOUNT = 3



# def fetch_videos(iterator, downloads_folder):
#   """Entry Point that handles everything related to the actual downloading operations

#   Args:
#       tasks_file (str): A File that contains information about the youtube downloads that must be executed
#       downloads_folder (str): A location for where to save the downloads
#   """


#   # Get Downloads items
#   downloadsDB = []

#   # Download item by item with retries on error
#   for item in iterator:
#     item_to_download = YoutubeDownloadItem().fromDict(item)

#     # This item was alreay downloaded
#     if item_to_download.isCompleted: 
#       downloadsDB.append(item_to_download)
#       continue

#     # Download with retries
#     for _ in range(RETRY_AMOUNT):
#       try:
#         logging.info(f"Downloading '{item_to_download.title}' at '{item_to_download.link}'")

#         # Perform Download, mark link as downloaded
#         fetch_video(item_to_download.link, item_to_download.stream_tag_of_interest, downloads_folder)
#         item_to_download.fromDict({"isCompleted": True, "completedAt": datetime.timestamp(datetime.now())})

#         logging.info(f"Download completed successfully at '{downloads_folder}\{item_to_download.title}'")
#         break
#       except Exception as e: 
#         logging.warning(f"Link '{item_to_download.link }' could not be downloaded. Re-attempting in {RETRY_PERIOD}sec")  
#         time.sleep(RETRY_PERIOD)
#         pass
    
#     # Display app's inability to process this link
#     if not item_to_download.isCompleted: logging.error(f"Permanent Error trying to download '{item_to_download.link}'") 
    
#     # Save current link object to database
#     downloadsDB.append(item_to_download)


#   return downloadsDB

# def fetch_video(link, stream_tag, location):
#   """Downloads a Video

#   Args:
#       link (string): Link to object to be downloaded
#       stream_tag (string): Stream Number to be downloaded
#       location (str): Where to save the video after download
#   """
#   # Connect to remote video, get stream of interest
#   yt = YouTube(link)
#   ys = yt.streams.get_by_itag(stream_tag)
    
#   # Download
#   ys.download(location)
    


if __name__ == '__main__':
  it = em.ResultsIterator()
  for doc in it:
    print(doc)