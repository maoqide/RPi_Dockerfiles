#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python rain.py 5)" > /var/log/rain.txt && \
#echo $(python rain.py 5) 

#interval
sleep 3;
#sleep 1
done

