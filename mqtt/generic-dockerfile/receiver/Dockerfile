FROM armbuild/alpine

ENV MQTT_PORT 1883
ENV MQTT_KEEPALIVE_INTERVAL 60
ENV PATH $PATH:/root
WORKDIR /root

RUN apk add --update \
    python \
    python-dev \
    py2-pip \
    && rm -rf /var/cache/apk/*

RUN pip install paho-mqtt
ADD ./receive.py /root/receive.py
ADD ./receive.sh /root/receive.sh

ENTRYPOINT ["receive.sh"]
