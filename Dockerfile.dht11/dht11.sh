#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
#get H and T
#remove space,[ and ]
echo "$output$(python dht11.py 11 9 )" > /var/log/dht11.txt && \

#interval
sleep 3;

done
