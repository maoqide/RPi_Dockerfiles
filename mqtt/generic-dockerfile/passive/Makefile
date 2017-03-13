export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-subscriber .
run:
	docker run -d --privileged --env GPIO_PIN=20 --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/#' ${REPOSITORY}/rpi-mqtt-subscriber
