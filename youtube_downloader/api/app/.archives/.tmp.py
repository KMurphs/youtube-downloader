#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the Elasticsearch client library
from typing import Dict
from elasticsearch import Elasticsearch, exceptions

# import JSON and time
import json, time

# create a timestamp using the time() method
start_time = time.time()

# declare globals for the Elasticsearch client host
DOMAIN = "localhost"
PORT = 9200

# concatenate a string for the client's host paramater
host = str(DOMAIN) + ":" + str(PORT)

# declare an instance of the Elasticsearch library
client = Elasticsearch(host)


start = 0
def reset_request(): 
    global start 
    start = 0
def build_request(query, size = 1): 
    global start
    start += size
    return {
        "from": start - size,
        "size": 1,
        "query": query
    }


class PowTwo:
    def __init__(self, max=0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        result = 2 ** self.n
        self.n += 1
        return result

def es_iterator(client: Elasticsearch, index = "videos", query: Dict = {"match_all": {}}, size = 1):
    reset_request()

    resp = client.search(
        index = index,
        body = build_request(query, size),
    )

    while len(resp['hits']['hits']):
        for doc in resp['hits']['hits']:
            yield doc

        resp = client.search(
            index = index,
            body = build_request(query, size),
        )

for i,j in enumerate(es_iterator(Elasticsearch(str(DOMAIN) + ":" + str(PORT)), query={ "bool": {"filter": [{ "term":  { "status": "0" }}]}	})):
    print(i, j.get('_source'), "\r\n")