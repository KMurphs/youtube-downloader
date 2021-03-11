from flask import Flask
import os
import logging

logging.basicConfig(level=logging.DEBUG,
                   format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                   datefmt='%Y-%m-%d %H:%M:%S',
                   handlers=[logging.StreamHandler()])

logger = logging.getLogger()

app = Flask(__name__)
import sys
logger.debug(__name__)
logger.debug("+++++++++++")
logger.debug(sys.path)
# print(sys.path)
# import os 
# print(os.environ)


# if(os.environ.get('FLASK_DEBUG') == "1"): 
#     # script path: os.path.dirname(os.path.realpath(__file__)) 
#     # script name: os.path.basename(os.path.realpath(__file__))
#     root = os.path.dirname(os.path.realpath(__file__))
#     sys.path[0] = root
#     # if(root not in sys.path):
#     #     sys.path.append(root)
#     #     pass
# print(sys.path)
# logger.debug(sys.path)
# import app.api
# from app import api
@app.route('/')
def hello_world():
    return 'Hello, World!'


# start the development server using the run() method
# if __name__ == "__main__":
# app.run(host="0.0.0.0", debug=True, port=5000)