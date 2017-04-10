FROM resin/rpi-raspbian:jessie

ENV PATH $PATH:/root
WORKDIR /root

ENV INTERVAL=1 DISPLAY=1
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ADD ./rtc-pi /root/rtc-pi
ADD ./ds1302.sh /root/ds1302.sh
ENTRYPOINT ["ds1302.sh"]

