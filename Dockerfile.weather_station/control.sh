#!/bin/sh

if [ ! -n "$PM25_THRESHOLD" ]; then
  PM25_THRESHOLD=71
fi

if [ ! -n "$TEMP_THRESHOLD" ]; then
  TEMP_THRESHOLD=40
fi

while true;
do

#main
python control.py $GPIO_DHT $GPIO_RAIN $PM25_THRESHOLD $TEMP_THRESHOLD

sleep $INTERVAL
done
