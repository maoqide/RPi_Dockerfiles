FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./hc_sr04.py /root/hc_sr04.py
ADD ./hc_sr04.sh /root/hc_sr04.sh

ENTRYPOINT ["hc_sr04.sh"]

