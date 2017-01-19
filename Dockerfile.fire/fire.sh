#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python fire.py $GPIO_PIN)" > /var/log/fire.txt && \

#interval
sleep $INTERVAL;
done

