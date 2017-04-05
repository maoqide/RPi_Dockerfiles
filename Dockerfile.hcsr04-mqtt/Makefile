export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-hcsr04 .
run:
	docker run -d --privileged --env GPIO_PIN_TRIG=23 --env GPIO_PIN_ECHO=24 --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/hcsr04' --env DIST_THRESHOLD=30 ${REPOSITORY}/rpi-mqtt-hcsr04
run-display:
	docker run -d --privileged --env GPIO_PIN_TRIG=23 --env GPIO_PIN_ECHO=24 --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/hcsr04' --env MQTT_TOPIC_DISPLAY='test/hcsr04-display' --env DIST_THRESHOLD=30 ${REPOSITORY}/rpi-mqtt-hcsr04
