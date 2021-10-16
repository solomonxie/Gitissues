FROM python:3-alpine
MAINTAINER Solomon Xie <solomonxiewise@gmail.com>

RUN apk add --no-cache git openssh-client

# Install requirements
COPY requirements.txt /
RUN python3 -m pip install --no-cache-dir -r /requirements.txt

COPY id_rsa id_rsa.pub /root/.ssh/
RUN chmod 700 /root/.ssh/id_rsa*

COPY entry.sh /

CMD ["/bin/sh", "/entry.sh"]
