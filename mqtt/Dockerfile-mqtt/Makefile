export REPOSITORY=maoqide
build:
	docker build -t ${REPOSITORY}/mosquitto-alpine .
run:
	docker run --restart=always -d -p 1883:1883 ${REPOSITORY}/mosquitto-alpine
