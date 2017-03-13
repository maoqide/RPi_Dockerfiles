FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

RUN pip install paho-mqtt

ADD ./subscribe.py /root/subscribe.py
ADD ./subscribe.sh /root/subscribe.sh

ENTRYPOINT ["subscribe.sh"]
