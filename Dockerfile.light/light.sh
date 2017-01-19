#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python light.py $GPIO_PIN)" > /var/log/light.txt && \

#interval
sleep $INTERVAL;
done

