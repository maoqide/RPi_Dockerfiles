#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python avoid.py $GPIO_PIN)" > /var/log/avoid.txt && \

#interval
sleep $INTERVAL
done

