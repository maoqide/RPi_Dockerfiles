FROM armbuild/alpine
ENV PATH $PATH:/root
WORKDIR /root

RUN apk add --update \
    python \
    python-dev \
    py2-pip \
    musl-dev \
    gcc \
    && pip install RPi.GPIO \
    && rm -rf /var/cache/apk/*

CMD ["/bin/sh"]

