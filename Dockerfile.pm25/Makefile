export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-sensor-pm25 .
run:
	docker run -d --privileged -v /var/log:/var/log --env INTERVAL=3 ${REPOSITORY}/rpi-sensor-pm25
