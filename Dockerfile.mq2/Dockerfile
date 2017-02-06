FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./mq2.py /root/mq2.py
ADD ./mq2.sh /root/mq2.sh

ENTRYPOINT ["mq2.sh"]

