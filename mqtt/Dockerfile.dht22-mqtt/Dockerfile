FROM armbuild/alpine
ENV PATH $PATH:/root
WORKDIR /root
RUN apk add --update \
    build-base \
    python \
    python-dev \
    py-pip \
    git \
    && pip install paho-mqtt \
    && rm -rf /var/cache/apk/*
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install
ADD ./publish.py /root/publish.py
ADD ./dht22.py /root/dht22.py
ADD ./dht22.sh /root/dht22.sh
ENTRYPOINT ["dht22.sh"]
