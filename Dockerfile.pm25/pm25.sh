#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
#get PM2.5 only
#echo "$output$(python g3.py | grep "pm25_cf" | awk '{print $2}')" > /var/log/pm25_cf.txt && \

#get PM1, PM2.5 and PM10
#remove space,[ and ]
echo "$output$(python g3.py | sed 's/ //g;s/\[//;s/\]//')" > /var/log/pm25_cf.txt && \

#interval
sleep $INTERVAL;

done
