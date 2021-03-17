import json
import os
# src_file = 'app\\api.py'
dst_file = 'app\\routes.json'

import sys


def route_doc(route):
    bare = (route.replace("@app.route('", "").replace("')","").replace(", methods=['","").replace("'])","").replace("\n","").replace("\r","") + "'GET").split("'")
    return {"path": bare[0].replace("<", "&lt").replace(">", "&gt"), "method": bare[1]}


def get_routes(src_file: str, do_write_to_file=False):
    routes = None
    with open(src_file, 'r') as f:
        routes = [route_doc(line) for line in f.readlines() if "@app.route" in line]
    if do_write_to_file: 
        dst_file = src_file.replace(".py", "_routes.json")
        with open(dst_file, 'w') as f: 
            json.dump(routes, f, indent=4, sort_keys=True)
    return routes