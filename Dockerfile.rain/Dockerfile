FROM maoqide/rpi_gpio

ENV PATH $PATH:/root
WORKDIR /root

ADD ./rain.py /root/rain.py
ADD ./rain.sh /root/rain.sh

ENTRYPOINT ["rain.sh"]

