#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python rain.py $GPIO_PIN)" > /var/log/rain.txt && \

#interval
sleep $INTERVAL;
done

