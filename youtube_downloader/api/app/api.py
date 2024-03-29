# https://github.com/microsoft/pylance-release/issues/236#issuecomment-759828693
import json
import logging
from flask import Flask, request
from __init__ import setup_logging
import urllib3
import urllib
from utils.utils import str_to_filename
import utils.video_manager as vm
# import utils.elasticsearch_manager as em 
import utils.routes_from_file as rff
import utils.zip as zip
import os


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
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(data), indent=4), 200, {'ContentType':'application/json'}

@app.route('/videos/id/<id>')
def get_by_id(id = None): 
    data, has_error = try_action(lambda: vm.get_video_by_id(id))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(data), indent=4), 200, {'ContentType':'application/json'}

@app.route('/videos/id/<id>', methods=['PUT'])
def update_video(id = None): 

    # Extract and validate data
    data, has_error = try_action(lambda: vm.video_from_user_data(request.json))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}

    # Have we processed this link before?    
    data, has_error = try_action(lambda: vm.get_video_by_id(id))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    if data.get('total') == 0: return json.dumps({"message": "Unknown ID"}, indent=4), 400, {'ContentType':'application/json'}

    # Process submission and validate results
    data, has_error = try_action(lambda: vm.process_video(data, is_new=False))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
        
    # Commit results
    data, has_error = try_action(lambda: vm.update_video(id, data))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(data, indent=4), 200, {'ContentType':'application/json'}



@app.route('/videos/new', methods=['POST'])
def new_video(): return add_video(request.json)

@app.route('/videos/new/bulk', methods=['POST'])
def new_videos(): 
    results = [ add_video(video) for video in request.json ]
    response = {
        "failed": [ res[0] for res in results if res[1] != 201],
        "created": [ res[0] for res in results if res[1] == 201]
    }
    return json.dumps({"results": response}, indent=4), 200, {'ContentType':'application/json'}

def add_video(user_data): 

    # Extract and validate data
    data, has_error = try_action(lambda: vm.video_from_user_data(user_data))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    logging.info(f'Processing user data: \'{json.dumps(data)}\'')
    link = data.get('url')

    # Have we processed this link before?    
    _data, has_error = try_action(lambda: vm.get_video_by_url(link))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    if _data.get('total') != 0: return json.dumps(_data), 200, {'ContentType':'application/json'}
    logging.info(f"Link '{link}' has not been processed before")

    # Process submission and validate results
    data, has_error = try_action(lambda: vm.process_video(data, is_new=True))
    if has_error: return json.dumps({"message":data}), has_error, {'ContentType':'application/json'}
    logging.info(f"Link '{link}' has been successfully processed: {json.dumps(data)}")

    # Commit results
    data, has_error = try_action(lambda: vm.create_video(data))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
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
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(json.loads(data.data.decode('utf-8'))), indent=4), 200, {'ContentType':'application/json'}

@app.route('/videos')
@app.route('/videos/')
def get_videos(): 
    logging.debug("Retrieving videos")
    query = urllib.parse.unquote(request.query_string.decode('utf-8')).replace("=", ":").replace("&", " AND ")
    encoded_args = urllib.parse.urlencode({'q': query if query is not "" else "*=*"})
    http = urllib3.PoolManager()
    logging.debug(f"Retrieving videos with: {json.dumps({'q': query})}")
    
    # data, has_error = try_action(lambda: http.request('GET', f'http://youtube_downloader_elasticsearch_app_1:9200/videos/_search?{encoded_args}'))
    data, has_error = try_action(lambda: http.request('GET', vm.get_search_url(args=encoded_args)))
    if has_error: return json.dumps({"message": "Could not process request", "data": data}, indent=4), has_error, {'ContentType':'application/json'}
    return json.dumps(vm.to_VideoRecord(json.loads(data.data.decode('utf-8'))), indent=4), 200, {'ContentType':'application/json'}

@app.route('/ping')
def ping(): return json.dumps({"code":200, "reply": "pong", "host": "backend"}, indent=4), 200, {'ContentType':'application/json'}


@app.route("/zip", methods=['POST'])
def archive(): 
    logging.debug("Zipping videos")

    manifest = [ vm.get_name_from_id(id) for id in request.json ]
    logging.debug(f"Zip Manifest: {json.dumps(manifest)}")


    bundle_name, bundle_path, bundle_url = vm.get_zipfile_details(url_root=request.url_root)
    _data, has_error = try_action(lambda: zip.from_iterator(bundle_path, [ (vm.get_name_from_id(id), vm.get_path_from_id(id)) for id in request.json ] + [("manifest.json", {"manifest": manifest})]))
    if has_error: return json.dumps({"message": "Could not bundles videos", "data": _data}, indent=4), has_error, {'ContentType':'application/json'}
    logging.debug(f"Bundle accessible at: {bundle_url}")
    return json.dumps({"link": bundle_url}, indent=4), 200, {'ContentType':'application/json'}


@app.route('/')
@app.route("/", defaults={"path": ""})
@app.route("/<string:path>") 
@app.route("/<path:path>")
def home(): return json.dumps({"approutes": rff.get_routes(__file__)}, indent=4), 200, {'ContentType':'application/json'}

# https://code-maven.com/python-flask-catch-exception
@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return json.dumps({"code":500, "message": "Unexpected Error Occured"}, indent=4), 200, {'ContentType':'application/json'}