export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-receiver .
run:
	docker run -d --privileged --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/#' ${REPOSITORY}/rpi-mqtt-receiver
