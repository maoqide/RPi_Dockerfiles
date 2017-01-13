FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./avoid.py /root/avoid.py
ADD ./avoid.sh /root/avoid.sh

ENTRYPOINT ["avoid.sh"]

