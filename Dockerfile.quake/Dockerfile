FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./quake.py /root/quake.py
ADD ./quake.sh /root/quake.sh

ENTRYPOINT ["quake.sh"]

