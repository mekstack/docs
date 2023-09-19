FROM python:alpine
RUN apk add --no-cache git
RUN pip install tox sphinx
