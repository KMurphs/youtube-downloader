FROM nginx:latest

COPY ./default.conf /etc/nginx/conf.d/default.conf

COPY ./assets/ /var/www/html/assets/

COPY ./includes/ /etc/nginx/includes/

COPY ./ssl/ /etc/ssl/certs/nginx/