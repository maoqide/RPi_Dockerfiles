#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python fire.py 5)" > /var/log/fire.txt && \
#echo $(python fire.py 5) 

#interval
sleep 3;
#sleep 1
done

