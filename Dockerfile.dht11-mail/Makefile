export REPOSITORY=localtest
export MAILTO_LIST=qmao@linkernetworks.com
export SMTPSERVER=smtp.qiye.163.com
export MAILHOST=qmao@linkernetworks.com
export PASSWORD=Mao940715

build:
	docker build -t  ${REPOSITORY}/rpi-dht11-mail .
run-example:
	docker run --restart=always --privileged -d --env GPIO_PIN=18 --env SEND_INTERVAL=300 --env INTERVAL=3 --env THRESHOLD=24 --env MAILTO_LIST=${MAILTO_LIST} --env SMTPSERVER=${SMTPSERVER} --env MAILHOST=${MAILHOST} --env PASSWORD=${PASSWORD} ${REPOSITORY}/rpi-dht11-mail
