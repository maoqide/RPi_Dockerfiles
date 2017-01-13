#!/bin/sh
while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python sr501.py 10)" > /var/log/hc_sr501.txt && \

#interval
sleep 3;

done

