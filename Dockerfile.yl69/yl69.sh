#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python yl69.py $GPIO_PIN)" > /var/log/yl69.txt && \

#interval
sleep $INTERVAL;

done

