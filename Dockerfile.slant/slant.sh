#!/bin/sh

while true;
do

#init
output=$(date +%s) && \

#seprator
output="$output," && \

#main
echo "$output$(python slant.py 5)" > /var/log/slant.txt && \
#echo $(python slant.py 5)

#interval
sleep 3

done

