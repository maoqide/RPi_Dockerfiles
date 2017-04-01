export REPOSITORY=localtest
build:
	docker build -t  ${REPOSITORY}/mqtt-auto-watering .
run:
	docker run -d --restart=always --privileged --env GPIO_FLOW=12 --env GPIO_SOIL=20 --env MQTT_BROKER=192.168.10.245 --env MQTT_PORT=1883 --env MQTT_KEEPALIVE_INTERVAL=60 --env MQTT_TOPIC='test/auto-watering' ${REPOSITORY}/mqtt-auto-watering
