#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python light.py 5)" > /var/log/light.txt && \
#echo $(python light.py 5) 

#interval
sleep 3;
#sleep 1
done

