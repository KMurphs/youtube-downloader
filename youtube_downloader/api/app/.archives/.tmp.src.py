#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# import the Elasticsearch client library
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
def get_request(): 
    global start
    size = 1
    start += size
    return {
        "from": start - size,
        "size": 1,
        "query": {
            "match_all": {}
        }
    }
try:
    # use the JSON library's dump() method for indentation
    info = json.dumps(client.info(), indent=4)

    # pass client object to info() method
    print ("Elasticsearch client info():", info)

except exceptions.ConnectionError as err:

    # print ConnectionError for Elasticsearch
    print ("\nElasticsearch info() ERROR:", err)
    print ("\nThe client host:", host, "is invalid or cluster is not running")

    # change the client's value to 'None' if ConnectionError
    client = None

# valid client instance for Elasticsearch
if client != None:

    # get all of the indices on the Elasticsearch cluster
    all_indices = client.indices.get_alias("*")

    # keep track of the number of the documents returned
    doc_count = 0

    reset_request()

    # iterate over the list of Elasticsearch indices
    for num, index in enumerate(all_indices):

        # declare a filter query dict object
        match_all = {
            "from": 0,
            "size": 1,
            "query": {
                "match_all": {}
            }
        }
        


        # make a search() request to get all docs in the index
        resp = client.search(
            index = index,
            # body = match_all,
            body = get_request(),
            # scroll = '2s' # length of time to keep search context
        )

        # keep track of pass scroll _id
        old_scroll_id = 1#resp['_scroll_id']
        print(resp)

        # use a 'while' iterator to loop over document 'hits'
        while len(resp['hits']['hits']):

            # # make a request using the Scroll API
            # resp = client.scroll(
            #     scroll_id = old_scroll_id,
            #     scroll = '2s' # length of time to keep search context
            # )

            # # check if there's a new scroll ID
            # if old_scroll_id != resp['_scroll_id']:
            #     print ("NEW SCROLL ID:", resp['_scroll_id'])

            # # keep track of pass scroll _id
            # old_scroll_id = resp['_scroll_id']

            # print the response results
            print ("\nresponse for index:", index)
            # print ("_scroll_id:", resp['_scroll_id'])
            print ('response["hits"]["total"]:', resp["hits"]["total"])
            print (resp)

            # iterate over the document hits for each 'scroll'
            for doc in resp['hits']['hits']:
                print ("\n", doc['_id'], doc['_source'])
                doc_count += 1
                print ("DOC COUNT:", doc_count)

            resp = client.search(
                index = index,
                # body = match_all,
                body = get_request(),
                # scroll = '2s' # length of time to keep search context
            )

    # print the total time and document count at the end
    print ("\nTOTAL DOC COUNT:", doc_count)

# print the elapsed time
print ("TOTAL TIME:", time.time() - start_time, "seconds.")