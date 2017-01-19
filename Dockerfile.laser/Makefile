export REPOSITORY=localtest
build:
	docker build -t  ${REPOSITORY}/rpi-laser .
run-example:
	docker run --restart=always --privileged -v /var/log:/var/log --env GPIO_PIN=12 --env INTERVAL=1 -d ${REPOSITORY}/rpi-laser
