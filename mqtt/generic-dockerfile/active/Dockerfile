FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

RUN pip install paho-mqtt

ADD ./publish.py /root/publish.py
ADD ./publish.sh /root/publish.sh

ENTRYPOINT ["publish.sh"]
