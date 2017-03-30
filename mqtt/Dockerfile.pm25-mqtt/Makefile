export REPOSITORY=localtest

build:
	docker build -t ${REPOSITORY}/rpi-mqtt-pm25 .
run:
	docker run -d --privileged --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/pm' --env PM25_THRESHOLD=50 ${REPOSITORY}/rpi-mqtt-pm25
