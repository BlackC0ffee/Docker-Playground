FROM nginx
COPY html /usr/share/nginx/html
RUN echo "Hello World from $(hostname)"
RUN curl -s http://eth0.me -o /usr/share/nginx/html/eth.html