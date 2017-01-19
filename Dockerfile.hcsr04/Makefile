export REPOSITORY=localtest
build:
	docker build -t  ${REPOSITORY}/rpi-sensor-hcsr04 .
run-example:
	docker run --restart=always --privileged -v /var/log:/var/log --env GPIO_PIN_TRIG=23 --env GPIO_PIN_ECHO=24 --env INTERVAL=3 -d ${REPOSITORY}/rpi-sensor-hcsr04
