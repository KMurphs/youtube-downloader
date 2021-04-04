import logging
from __init__ import setup_logging_to_file
import utils.video_manager as vm

# setup_logging(logging.INFO)
setup_logging_to_file(logging.DEBUG, file="/youtube_downloader/logs/logs.log")
vm.download_videos()