FROM resin/rpi-raspbian:jessie

WORKDIR /root
RUN apt-get update -y &&\
    apt-get install -y python &&\
    apt-get install -y python-dev &&\
    apt-get install -y python-pip &&\
    apt-get install -y python-picamera &&\
    rm -rf /var/cache/apt

EXPOSE 15001
ADD ./pistreaming.py /root/pistreaming.py
ENTRYPOINT ["python", "pistreaming.py"]

