#!/bin/sh
while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python sr501.py $GPIO_PIN)" > /var/log/hc_sr501.txt && \

#interval
sleep $INTERVAL;

done

