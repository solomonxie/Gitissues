FROM python:3-alpine

MAINTAINER Solomon Xie <solomonxiewise@gmail.com>

RUN apk add git

RUN git clone https://github.com/solomonxie/issues_blog.git && \
    git clone https://github.com/solomonxie/gitissues.git

RUN pip install requests

CMD /bin/bash
