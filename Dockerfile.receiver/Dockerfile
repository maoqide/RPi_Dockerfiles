FROM armbuild/alpine

ENV PATH $PATH:/root
WORKDIR /root

ENV INTERVAL 1
ADD ./receive.sh /root/receive.sh
ENTRYPOINT ["receive.sh"]
