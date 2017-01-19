export REPOSITORY=localtest
build:
	docker build -t  ${REPOSITORY}/rpi-sensor-rain .
run-example:
	docker run --restart=always --privileged -v /var/log:/var/log --env GPIO_PIN=5 --env INTERVAL=3 -d ${REPOSITORY}/rpi-sensor-rain
