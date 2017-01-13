FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./light.py /root/light.py
ADD ./light.sh /root/light.sh

ENTRYPOINT ["light.sh"]

