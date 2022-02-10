FROM php:7.2-apache
WORKDIR /var/www/html/
COPY /docuwiki /var/www/html/
RUN chmod -R 777 data/
RUN chmod -R 777 lib/
RUN chmod -R 777 conf/