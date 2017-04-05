FROM resin/rpi-raspbian:jessie

ENV MQTT_PORT 1883
ENV MQTT_KEEPALIVE_INTERVAL 60
ENV PATH $PATH:/root
WORKDIR /root

RUN apt-get update -y &&\
    apt-get install -y python &&\
    apt-get install -y python-dev &&\
    apt-get install -y python-pip &&\
    apt-get install -y python-picamera &&\
    rm -rf /var/cache/apt

RUN pip install paho-mqtt
ADD ./capture.py /root/capture.py
ADD ./capture.sh /root/capture.sh

ENTRYPOINT ["capture.sh"]
