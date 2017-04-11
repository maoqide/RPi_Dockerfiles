export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-sensor-waterflow .
run:
	docker run -d --privileged -v /var/log:/var/log --env GPIO_PIN=12 ${REPOSITORY}/rpi-sensor-waterflow
