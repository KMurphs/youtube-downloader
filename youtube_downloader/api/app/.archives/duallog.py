import logging
import time
import os

# CRITICAL 	50
# ERROR 	  40
# WARNING 	30
# INFO 	    20
# DEBUG 	  10
# NOTSET 	  0
# logging.basicConfig(level=logging.INFO, format='[%(asctime)s.%(msecs)03d][%(levelname)-5s]: %(message)s', datefmt='%H:%M:%S') 
# logging.Formatter.converter = time.gmtime

# https://stackoverflow.com/a/13733863
# https://github.com/acschaefer/duallog
def setupLogger(logFileDir = ".", logFileName = "app.log", console_level = logging.DEBUG, file_level = logging.INFO):

   
  
  # logFormatter = logging.Formatter("[%(asctime)s.%(msecs)03d][%(threadName)-12.12s][%(levelname)-5.5s]  %(message)s")
  logFormatter = logging.Formatter("[%(asctime)s.%(msecs)03d][%(levelname)-5s]:  %(message)s", datefmt='%H:%M:%S') 
  logFormatter.converter = time.gmtime
  rootLogger = logging.getLogger()
  rootLogger.setLevel(logging.NOTSET)

  fileHandler = logging.FileHandler(os.path.join(logFileDir, logFileName))
  fileHandler.setFormatter(logFormatter)
  fileHandler.setLevel(file_level)
  rootLogger.addHandler(fileHandler)

  consoleHandler = logging.StreamHandler()
  consoleHandler.setFormatter(logFormatter)
  consoleHandler.setLevel(console_level)
  rootLogger.addHandler(consoleHandler)
