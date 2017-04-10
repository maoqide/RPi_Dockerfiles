export REPOSITORY=localtest
build:
	docker build -t  ${REPOSITORY}/rpi-sensor-receiver .
run:
	docker run -d --restart=always -v /var/log:/var/log --env SENSOR=dht11 --env INTERVAL=1 ${REPOSITORY}/rpi-sensor-receiver
