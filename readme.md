
## Commands

### docker
docker-compose build
docker-compose up -d
docker cp zealous_mirzakhani:/etc/nginx/ .\backend\intro\binds\nginx\
docker cp relaxed_shaw:/etc/nginx/ .\backend\intro\binds\

docker exec -it <container name> <command>
docker exec -it reverse_proxy_1 nginx -s reload

docker container logs -f --details youtube_downloader_backend_app_1

### openssl
C:\Program Files\Git\usr\bin\openssl.exe
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout example1.key -out example1.crt



### elasticsearch
curl http://localhost:9200/_cluster/health
curl http://localhost:9200/_aliases?pretty
curl -X PUT "localhost:9200/customer/_doc/1?pretty" -H 'Content-Type: application/json' -d'{"name": "Mark Heath" }'
curl http://localhost:9200/customer/_doc/1?pretty
curl http://localhost:9200/customer/_search?pretty
curl -XDELETE http://localhost:9200/customer/_doc/1?pretty
curl -XDELETE http://localhost:9200/customer/
curl -XPOST http://localhost:9200/customer/_doc -H "Content-Type: application/json" -d @test.json

/customers/customer/some-id??
/index/type/id


elasticdump \
    --input=http://localhost:9200/sample_index \
    --output=/Users/retina/Desktop/sample_file.json \
    --type=data
elasticdump     --input=http://localhost:9200/customer     --output=data/iodata/file.json     --type=data
elasticdump     --input=http://localhost:9200/customer     --output=data/iodata/file.json     --type=mapping
docker exec -it youtube_downloader_elasticsearch_app_1 curl http://localhost:9200/_cluster/health?pretty
curl http://localhost:9200/_cluster/health?pretty



curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "from": 5,
  "size": 20,
  "query": {
    "match": {
      "user.id": "kimchy"
    }
  }
}
'
curl -X GET "localhost:9200/customer/_search?pretty" -H 'Content-Type: application/json' -d'{"from": 5,"size": 20}'

curl -X PUT "localhost:9200/customer/_doc/1?pretty"  -H 'Content-Type: application/json' -d'{"name": "Mark Heath" }'

curl "localhost:9200/customer/_search?pretty" -H "Content-Type: application/json" -d"{\"from\": 1,\"size\": 4}"


# Resources

https://www.freecodecamp.org/news/docker-nginx-letsencrypt-easy-secure-reverse-proxy-40165ba3aee2/
https://www.freecodecamp.org/news/docker-compose-nginx-and-letsencrypt-setting-up-website-to-do-all-the-things-for-that-https-7cb0bf774b7e/
https://phoenixnap.com/kb/docker-nginx-reverse-proxy
https://docs.microsoft.com/en-us/windows/wsl/install-win10
https://docs.docker.com/docker-for-windows/wsl/
https://www.youtube.com/watch?v=hcw-NjOh8r0&list=LL&index=3
https://discuss.elastic.co/t/iterating-over-all-data/13610/3
https://www.elastic.co/guide/en/elasticsearch/reference/current/paginate-search-results.html
https://github.com/microsoft/pylance-release/issues/236#issuecomment-759828693
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
https://blog.theodo.com/2020/05/debug-flask-vscode/
https://github.com/PyBackendBoilerplate/micro-service