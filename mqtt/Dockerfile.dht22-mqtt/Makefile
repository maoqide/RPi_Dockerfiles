export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-dht22 .
run:
	docker run -d --privileged --env GPIO_PIN=4 --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/dht22' --env TEMP_THRESHOLD=20 ${REPOSITORY}/rpi-mqtt-dht22
run-display:	
	docker run -d --privileged --env GPIO_PIN=4 --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/dht22' --env TEMP_THRESHOLD=20 --env MQTT_TOPIC_DISPLAY='test/dht-display' ${REPOSITORY}/rpi-mqtt-dht22
