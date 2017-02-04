FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./laser.py /root/laser.py
ADD ./laser.sh /root/laser.sh

ENTRYPOINT ["laser.sh"]

