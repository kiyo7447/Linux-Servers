FROM alpine:latest

RUN apk add --no-cache curl
RUN curl -L -o /usr/local/bin/mkcert https://github.com/FiloSottile/mkcert/releases/download/v1.4.3/mkcert-v1.4.3-linux-amd64
RUN chmod +x /usr/local/bin/mkcert
RUN mkcert -install

ENTRYPOINT ["mkcert"]
