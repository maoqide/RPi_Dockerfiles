#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python yl69.py 5)" > /var/log/yl69.txt && \

#interval
sleep 3;

done

