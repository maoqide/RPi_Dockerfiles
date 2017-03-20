FROM armbuild/alpine
ENV PATH $PATH:/root
WORKDIR /root
RUN apk add --update \
    python \
    py-pip \
  && pip install pyserial \
  && pip install paho-mqtt \
  && rm -rf /var/cache/apk/*
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install
ADD . /root
ENTRYPOINT ["control.sh"]
