FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY test /test
WORKDIR /test
EXPOSE 8000

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password test-user

USER test-user
