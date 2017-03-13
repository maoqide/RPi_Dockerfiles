FROM armbuild/alpine

WORKDIR /root
EXPOSE 1883

RUN apk add --update mosquitto \
    && rm -rf /var/cache/apk/*

ADD ./mosquitto.conf /root/mosquitto.conf

ENTRYPOINT ["/usr/sbin/mosquitto", "-c", "/root/mosquitto.conf"]
