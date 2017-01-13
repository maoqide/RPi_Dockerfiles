#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python hc_sr04.py 23 24)" > /var/log/hc_sr04.txt && \

#interval
sleep 3;

done

