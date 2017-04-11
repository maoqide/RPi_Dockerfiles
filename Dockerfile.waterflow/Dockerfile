FROM maoqide/rpi-gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./waterflow.py /root/waterflow.py
ADD ./waterflow.sh /root/waterflow.sh

ENTRYPOINT ["waterflow.sh"]
