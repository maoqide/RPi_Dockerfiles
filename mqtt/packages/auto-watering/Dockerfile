FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

RUN pip install paho-mqtt

ADD ./auto-water.py /root/auto-water.py
ADD ./auto-watering.sh /root/auto-watering.sh

ENTRYPOINT ["auto-watering.sh"]
