FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./sr501.py /root/sr501.py
ADD ./sr501.sh /root/sr501.sh

ENTRYPOINT ["sr501.sh"]
