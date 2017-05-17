export REPOSITORY=localtest
export COMPOSE_HTTP_TIMEOUT=300

build:
	docker build -t ${REPOSITORY}/rpi-moto .
run:
	docker run --privileged -d --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test' ${REPOSITORY}/rpi-moto .
up:
	docker-compose up -d
down:
	docker-compose down

