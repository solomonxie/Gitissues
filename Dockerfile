FROM python:3-alpine

MAINTAINER Solomon Xie <solomonxiewise@gmail.com>

RUN apk add git

RUN git clone https://github.com/solomonxie/issues_blog.git
COPY . /src

RUN python3 -m pip install -f requirements.txt

CMD /bin/bash
