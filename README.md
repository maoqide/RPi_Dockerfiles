# RPi_Dockerfiles

## example:
```shell
#build image
cd Dockerfile.light
sudo docker build -t maoqide/light .

#run
docker run --restart=always --privileged -v /var/log:/var/log --env GPIO_PIN=5 --env INTERVAL=3 -d maoqide/light
```
