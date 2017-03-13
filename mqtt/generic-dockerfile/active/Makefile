export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-publisher .
run:
	docker run -d --privileged --env GPIO_PIN=17 --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/light' ${REPOSITORY}/rpi-mqtt-publisher
run-full:
	docker run -d --privileged --env GPIO_PIN=17 --env MQTT_BROKER=192.168.10.245 --env MQTT_PORT=1883 --env MQTT_KEEPALIVE_INTERVAL=60 --env MQTT_TOPIC='test/light' --env SIGNAL_DO=1 ${REPOSITORY}/rpi-mqtt-publisher
