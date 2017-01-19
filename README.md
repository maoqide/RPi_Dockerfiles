# RPi_Dockerfiles

## example:
```shell
#build image
cd Dockerfile.hcsr04
sudo docker build -t maoqide/hcsr04 .

#run
sudo docker run --privileged -v /var/log:/var/log -d maoqide/hcsr04
```
