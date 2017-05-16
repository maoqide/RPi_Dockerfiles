export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-moto .
run:
	docker run --privileged -d --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test' ${REPOSITORY}/rpi-moto .
