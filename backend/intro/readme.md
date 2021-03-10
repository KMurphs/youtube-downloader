
## Commands
docker-compose build
docker-compose up -d
docker cp zealous_mirzakhani:/etc/nginx/ .\backend\intro\binds\nginx\
docker cp relaxed_shaw:/etc/nginx/ .\backend\intro\binds\

docker exec -it <container name> <command>
docker exec -it reverse_proxy_1 nginx -s reload

C:\Program Files\Git\usr\bin\openssl.exe

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout example1.key -out example1.crt

# Resources

https://www.freecodecamp.org/news/docker-nginx-letsencrypt-easy-secure-reverse-proxy-40165ba3aee2/
https://www.freecodecamp.org/news/docker-compose-nginx-and-letsencrypt-setting-up-website-to-do-all-the-things-for-that-https-7cb0bf774b7e/
https://phoenixnap.com/kb/docker-nginx-reverse-proxy
https://docs.microsoft.com/en-us/windows/wsl/install-win10
https://docs.docker.com/docker-for-windows/wsl/
https://www.youtube.com/watch?v=hcw-NjOh8r0&list=LL&index=3
