FROM armbuild/alpine
ENV PATH $PATH:/root
WORKDIR /root
RUN apk add --update \
    python \
    py-pip \
  && pip install pyserial \
  && rm -rf /var/cache/apk/*
ADD ./g3.py /root/g3.py
ADD ./pm25.sh /root/pm25.sh
ENTRYPOINT ["pm25.sh"]
