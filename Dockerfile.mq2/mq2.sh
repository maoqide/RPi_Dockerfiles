#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python mq2.py $GPIO_PIN)" > /var/log/mq2.txt && \

#interval
sleep $INTERVAL
done

