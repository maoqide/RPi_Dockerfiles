#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python voice.py $GPIO_PIN)" > /var/log/voice.txt && \

#interval
sleep $INTERVAL;
done

