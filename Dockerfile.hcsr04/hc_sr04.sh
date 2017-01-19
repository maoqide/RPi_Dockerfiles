#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python hc_sr04.py $GPIO_PIN_TRIG $GPIO_PIN_ECHO)" > /var/log/hc_sr04.txt && \

#interval
sleep $INTERVAL;

done

