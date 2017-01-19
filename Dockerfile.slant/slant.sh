#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python slant.py $GPIO_PIN)" > /var/log/slant.txt && \

#interval
sleep $INTERVAL;
done

