# https://github.com/microsoft/pylance-release/issues/236#issuecomment-759828693
import json
import logging
from flask import Flask, request
from __init__ import setup_logging
import urllib3
import urllib
import utils.video_manager as vm
# import utils.elasticsearch_manager as em 
import utils.routes_from_file as rff


logger = setup_logging()
app = Flask(__name__)


def try_action(action_fn):
    try: return (action_fn(), 0)
    except Exception as e:
        logging.error(e)
        code, reason, *_ = e.args
        return (reason, code)








@app.route('/videos/url/<url>')
def get_by_url(url = None): 
    data, has_error = try_action(lambda: vm.get_video_by_url(url))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(data), indent=4), 200, {'ContentType':'application/json'}

@app.route('/videos/id/<id>')
def get_by_id(id = None): 
    data, has_error = try_action(lambda: vm.get_video_by_id(id))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(data), indent=4), 200, {'ContentType':'application/json'}

@app.route('/videos/id/<id>', methods=['PUT'])
def update_video(id = None): 

    # Extract and validate data
    data, has_error = try_action(lambda: vm.video_from_user_data(request.json))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}

    # Have we processed this link before?    
    data, has_error = try_action(lambda: vm.get_video_by_id(id))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    if data.get('total') == 0: return json.dumps({"message": "Unknown ID"}, indent=4), 400, {'ContentType':'application/json'}

    # Process submission and validate results
    data, has_error = try_action(lambda: vm.process_video(data, is_new=False))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
        
    # Commit results
    data, has_error = try_action(lambda: vm.update_video(id, data))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(data, indent=4), 200, {'ContentType':'application/json'}



@app.route('/videos/new', methods=['POST'])
def new_video(): return add_video(request.json)

@app.route('/videos/new/bulk', methods=['POST'])
def new_videos(): 
    results = [ add_video(video) for video in request.json ]
    response = {
        "failed": [ res[0] for res in results if res[1] != 0],
        "created": [ res[0] for res in results if res[1] == 0]
    }
    return json.dumps({"results": response}, indent=4), 200, {'ContentType':'application/json'}

def add_video(user_data): 

    # Extract and validate data
    data, has_error = try_action(lambda: vm.video_from_user_data(user_data))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    # logging.info(f'Processing user data: \'{json.dumps(data)}\'')
    logging.info('Processing user data: \'\'')
    link = data.get('url')

    # Have we processed this link before?    
    _data, has_error = try_action(lambda: vm.get_video_by_url(link))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    if _data.get('total') != 0: return json.dumps(_data), 200, {'ContentType':'application/json'}
    logging.info(f"Link '{link}' has not been processed before")

    # Process submission and validate results
    data, has_error = try_action(lambda: vm.process_video(data, is_new=True))
    if has_error: return json.dumps({"message":data}), has_error, {'ContentType':'application/json'}
    logging.info(f"Link '{link}' has been successfully processed: {json.dumps(data)}")

    # Commit results
    data, has_error = try_action(lambda: vm.create_video(data))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    logging.info(f"Link '{link}' has been successfully committed: {json.dumps(data)}")
    return json.dumps(data, indent=4), 201, {'ContentType':'application/json'}



@app.route('/videos/queries', methods=['POST'])
def get_videos_advanced(): 
    http = urllib3.PoolManager()
    encoded_data = json.dumps(request.json).encode('utf-8')
    logging.debug('Running elasticsearch query: '+ encoded_data.decode('utf-8'))
    
    data, has_error = try_action(lambda: http.request(
        'POST', 
        vm.get_search_url(prettify=True),
        body = encoded_data,
        headers = {'Content-Type': 'application/json'}
    ))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(json.loads(data.data.decode('utf-8'))), indent=4), 200, {'ContentType':'application/json'}

@app.route('/videos/')
def get_videos(): 
    query = urllib.parse.unquote(request.query_string.decode('utf-8')).replace("=", ":").replace("&", " AND ")
    encoded_args = urllib.parse.urlencode({'q': query})
    http = urllib3.PoolManager()
    
    # data, has_error = try_action(lambda: http.request('GET', f'http://youtube_downloader_elasticsearch_app_1:9200/videos/_search?{encoded_args}'))
    data, has_error = try_action(lambda: http.request('GET', vm.get_search_url(args=encoded_args)))
    if has_error: return json.dumps({"message": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(json.loads(data.data.decode('utf-8'))), indent=4), 200, {'ContentType':'application/json'}

@app.route('/ping')
def ping(): return json.dumps({"code":200, "reply": "pong", "host": "backend"}, indent=4), 200, {'ContentType':'application/json'}

@app.route('/')
def home(): return json.dumps({"approutes": rff.get_routes(__file__)}, indent=4), 200, {'ContentType':'application/json'}