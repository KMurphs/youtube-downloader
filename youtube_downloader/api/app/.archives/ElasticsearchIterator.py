from typing import Dict
from elasticsearch import Elasticsearch



def ESIterator(url: str = "localhost:9200", index = "videos", query: Dict = {"match_all": {}}, size = 1):
    
    
    client = Elasticsearch(url)
    start = 0
    def request():
        nonlocal start
        resp = client.search( index = index, body = { "from": start, "size": size, "query": query } )
        start += size
        return resp


    hits = 1
    while hits != 0:
        docs = request()
        hits = len(docs['hits']['hits'])
        for doc in docs['hits']['hits']: 
            yield doc
    


if __name__ == '__main__':
    # declare globals for the Elasticsearch client host
    DOMAIN = "localhost"
    PORT = 9200
    for j in ElasticsearchResultIterator(str(DOMAIN) + ":" + str(PORT), index="videos", query={ "bool": {"filter": [{ "term":  { "status": "0" }}]}	}):
        print(j.get('_source'), "\r\n")
