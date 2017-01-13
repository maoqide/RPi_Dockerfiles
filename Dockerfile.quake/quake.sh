#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python quake.py 5)" > /var/log/quake.txt && \
#echo $(python quake.py 5) 

#interval
sleep 3;
#sleep 1
done

