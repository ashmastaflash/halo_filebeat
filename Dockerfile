FROM alpine:3.4
MAINTAINER toolbox@cloudpassage.com



RUN apk update && apk add \
    gettext \
    python \
    py-pip

RUN apk add filebeat \
    --update-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing/

RUN pip install cloudpassage

COPY app/ /app

CMD app/runner.sh
