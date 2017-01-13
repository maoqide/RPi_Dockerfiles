#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python avoid.py 5)" > /var/log/avoid.txt && \
#echo $(python avoid.py 5) 

#interval
sleep 3;
#sleep 1
done

