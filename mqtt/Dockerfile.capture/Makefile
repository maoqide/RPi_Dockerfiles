export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-capture .
run:
	docker run -d --privileged --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/capture' ${REPOSITORY}/rpi-mqtt-capture
