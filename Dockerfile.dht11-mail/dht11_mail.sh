#!/bin/sh

while true; do
    temp=$(python dht11.py 11 $GPIO_PIN | cut -f1 -d.)
    echo temp: $temp
    if [[ -n "$temp" && "$temp" -gt "$THRESHOLD" ]]; then
	python smtp.py $MAILTO_LIST $SMTPSERVER $MAILHOST $PASSWORD
	sleep $SEND_INTERVAL;
    fi
    sleep $INTERVAL;
done
