export REPOSITORY=localtest
build:
	docker build -t  ${REPOSITORY}/rpi-sensor-dht11 .
run-example:
	docker run --restart=always --privileged -v /var/log:/var/log --env GPIO_PIN=9 --env INTERVAL=3 -d ${REPOSITORY}/rpi-sensor-dht11
