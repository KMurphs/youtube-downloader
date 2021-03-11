# https://github.com/microsoft/pylance-release/issues/236#issuecomment-759828693
from flask import Flask
from __init__ import setup_logging
# from . import setup_logging
import json



logger = setup_logging()
app = Flask(__name__)



@app.route('/ping')
def ping(): return json.dumps({"code":200, "reply": "pong", "host": "backend"}), 200, {'ContentType':'application/json'}




@app.route('/')
def home(): return 'Hello, World! from API'