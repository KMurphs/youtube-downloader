# https://github.com/microsoft/pylance-release/issues/236#issuecomment-759828693
import json
import logging
from flask import Flask, request
from __init__ import setup_logging
from utils.metadata import process_video, get_video_by_url, video_from_user_data
from utils.elasticsearch import create_video, get_video_by_id
import urllib3
import urllib


logger = setup_logging()
app = Flask(__name__)


def try_action(action_fn):
    try: return (action_fn(), 0)
    except Exception as e:
        logging.error(e)
        code, reason, *_ = e.args
        return (reason, code)



@app.route('/videos/new', methods=['POST'])
def add_video(): 

    # Extract and validate data
    data, has_error = try_action(lambda: video_from_user_data(request.json))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}

    # Have we processed this link before?    
    data, has_error = try_action(lambda: get_video_by_url(data.get('url')))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}
    if data["hits"]["total"] != 0: return json.dumps(data), 200, {'ContentType':'application/json'}

    # Process submission and validate results
    data, has_error = try_action(lambda: process_video(data, is_new=False))
    if has_error: return json.dumps({"message":data}), has_error, {'ContentType':'application/json'}
        
    # Commit results
    data, has_error = try_action(lambda: create_video(data))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}
    return json.dumps(data), 200, {'ContentType':'application/json'}






@app.route('/videos/url/<url>')
def get_by_url(url = None): 
    data, has_error = try_action(lambda: get_video_by_url(url))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}
    return json.dumps(data), 200, {'ContentType':'application/json'}

@app.route('/videos/id/<id>')
def get_by_id(id = None): 
    data, has_error = try_action(lambda: get_video_by_id(id))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}
    return json.dumps(data), 200, {'ContentType':'application/json'}
    
@app.route('/videos/')
def get_videos(): 
    query = urllib.parse.unquote(request.query_string.decode('utf-8')).replace("=", ":").replace("&", " AND ")
    encoded_args = urllib.parse.urlencode({'q': query})
    http = urllib3.PoolManager()
    
    # data, has_error = try_action(lambda: http.request('GET', f'http://youtube_downloader_elasticsearch_app_1:9200/videos/_search?{encoded_args}'))
    data, has_error = try_action(lambda: http.request('GET', f'http://localhost:9200/videos/_search?{encoded_args}'))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}
    return data.data.decode('utf-8'), data.status, {'ContentType':'application/json'}




@app.route('/videos/<id>', methods=['PUT'])
def update_video(id = None): 

    # Extract and validate data
    data, has_error = try_action(lambda: video_from_user_data(request.json))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}

    # Have we processed this link before?    
    data, has_error = try_action(lambda: get_video_by_id(id))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}
    if data["hits"]["total"] == 0: return f"{{\"message\":\"Unknown ID\"}}", 400, {'ContentType':'application/json'}

    # Process submission and validate results
    data, has_error = try_action(lambda: process_video(data, is_new=False))
    if has_error: return json.dumps({"message":data}), has_error, {'ContentType':'application/json'}
        
    # Commit results
    data, has_error = try_action(lambda: update_video(id, data))
    if has_error: return f"{{\"message\": {data}}}", has_error, {'ContentType':'application/json'}
    return json.dumps(data), 200, {'ContentType':'application/json'}

@app.route('/ping')
def ping(): return json.dumps({"code":200, "reply": "pong", "host": "backend"}), 200, {'ContentType':'application/json'}

@app.route('/')
def home(): return 'Hello, World! from API'