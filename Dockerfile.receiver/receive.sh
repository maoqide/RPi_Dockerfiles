#!/bin/sh

while true;
do
echo $(cat /var/log/${SENSOR}.txt)

sleep $INTERVAL

done
