FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./voice.py /root/voice.py
ADD ./voice.sh /root/voice.sh

ENTRYPOINT ["voice.sh"]

