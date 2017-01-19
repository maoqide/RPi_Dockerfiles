FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./slant.py /root/slant.py
ADD ./slant.sh /root/slant.sh

ENTRYPOINT ["slant.sh"]

