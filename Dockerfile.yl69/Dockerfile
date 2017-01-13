FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./yl69.py /root/yl69.py
ADD ./yl69.sh /root/yl69.sh

ENTRYPOINT ["yl69.sh"]

