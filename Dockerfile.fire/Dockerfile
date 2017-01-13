FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./fire.py /root/fire.py
ADD ./fire.sh /root/fire.sh

ENTRYPOINT ["fire.sh"]

