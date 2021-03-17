import logging
from __init__ import setup_logging
import utils.video_manager as vm

setup_logging(logging.INFO)
vm.download_videos()