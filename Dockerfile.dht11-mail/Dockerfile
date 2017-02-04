FROM armbuild/alpine
ENV PATH $PATH:/root
WORKDIR /root
RUN apk add --update \
    build-base \
    python \
    python-dev \
    git \
    && rm -rf /var/cache/apk/*
RUN git clone https://github.com/adafruit/Adafruit_Python_DHT.git
RUN cd Adafruit_Python_DHT && python setup.py install
ADD ./dht11.py /root/dht11.py
ADD ./smtp.py /root/smtp.py
ADD ./dht11_mail.sh /root/dht11_mail.sh
ENTRYPOINT ["dht11_mail.sh"]

