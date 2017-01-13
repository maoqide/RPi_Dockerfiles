#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python voice.py 5)" > /var/log/voice.txt && \
#echo $(python voice.py 5) 

#interval
sleep 3;
#sleep 1
done

