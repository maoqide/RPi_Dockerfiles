#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python quake.py $GPIO_PIN)" > /var/log/quake.txt && \

#interval
sleep $INTERVAL;
done

