FROM resin/rpi-raspbian:jessie

WORKDIR /root
RUN apt-get update -y &&\
    apt-get install -y python &&\
    apt-get install -y python-dev &&\
    apt-get install -y python-pip &&\
    apt-get install -y python-picamera &&\
    apt-get install -y tesseract-ocr && \
    apt-get install -y gcc && \
    apt-get install -y musl-dev && \
    rm -rf /var/cache/apt

RUN pip install paho-mqtt &&\
    pip install RPi.GPIO

ADD ./* /root/
ENTRYPOINT ["/root/control.sh"]
