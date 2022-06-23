# Install alpine, python3 and pip
FROM alpine:latest
LABEL maintainer="oppsec <https://github.com/oppsec>"
RUN apk add --no-cache python3 py3-pip

# Create directories
WORKDIR /Pinkerton
COPY . .

# Install libraries and run
RUN pip3 install -r requirements.txt
CMD ["python3", "main.py -h"]