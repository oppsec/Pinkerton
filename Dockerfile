FROM python:3.8-slim
LABEL maintainer="oppsec <https://github.com/oppsec>"

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PIP_NO_CACHE_DIR=off

WORKDIR /Pinkerton

RUN apt-get update && \
    apt-get install -y libffi-dev libxml2-dev libxslt-dev libssl-dev openssl autoconf g++ python3-dev libkrb5-dev git

# Create directories
COPY . .

# Install libraries and run
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py", "-h"]
