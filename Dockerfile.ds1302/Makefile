#DS1302		RASPBERRY PI
#CLK		GPIO21
#DAT		GPIO18
#RST		GPIO17
export REPOSITORY=localtest

build:
	docker build -t  ${REPOSITORY}/rpi-sensor-ds1302 .
run:
	docker run -d --privileged -v /var/log:/var/log --env INTERVAL=3 --env DISPLAY=1 --env SETTIME=`date +%Y%m%d%H%M%S` ${REPOSITORY}/rpi-sensor-ds1302
