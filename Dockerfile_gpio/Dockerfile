FROM armbuild/alpine
ENV PATH $PATH:/root
WORKDIR /root
RUN apk add --update \
    build-base \
    python \
    python-dev \
    && rm -rf /var/cache/apk/*
ADD ./RPi.GPIO-0.6.3 /root/RPi.GPIO-0.6.3
RUN cd /root/RPi.GPIO-0.6.3 && python setup.py install
CMD ["/bin/sh"]

