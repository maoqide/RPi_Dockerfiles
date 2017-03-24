export REPOSITORY=localtest
build:
	docker build -t  ${REPOSITORY}/ngiot-auto-watering .
run2:
	docker run -d --restart=always --privileged --env IOT_SERVER=192.168.10.245 --env GPIO_FLOW=12 --env GPIO_SOIL=20 --label=ngiot ${REPOSITORY}/ngiot-auto-watering
run:
	docker run -d --restart=always --privileged --net=host --env GPIO_FLOW=12 --env GPIO_SOIL=20 --label=ngiot ${REPOSITORY}/ngiot-auto-watering
