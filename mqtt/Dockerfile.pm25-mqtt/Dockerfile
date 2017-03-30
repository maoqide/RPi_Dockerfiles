FROM armbuild/alpine
ENV PATH $PATH:/root
WORKDIR /root
RUN apk add --update \
    python \
    py-pip \
  && pip install pyserial \
  && pip install paho-mqtt \
  && rm -rf /var/cache/apk/*
ADD ./g3.py /root/g3.py
ADD ./publish.py /root/publish.py
ADD ./pm25.sh /root/pm25.sh
CMD ["pm25.sh"]
