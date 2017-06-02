export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-pm25 .
run:
	docker run -d --privileged --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/pm' --env PM25_THRESHOLD=50 ${REPOSITORY}/rpi-mqtt-pm25
# TTY maybe ttyAMA0 or ttyS0, default ttyAMA0
run-custom-pm25-tty:
	docker run -d --privileged --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/pm' --env PM25_THRESHOLD=50 --env TTY=ttyS0 ${REPOSITORY}/rpi-mqtt-pm25
run-display:
	docker run -d --privileged --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/pm' --env PM25_THRESHOLD=50 --env MQTT_TOPIC_DISPLAY='test/pm-display' ${REPOSITORY}/rpi-mqtt-pm25
