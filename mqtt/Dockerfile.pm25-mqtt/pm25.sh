#!/bin/sh

#init variable
if [ ! -n "$MQTT_BROKER" ]||[ ! -n "$MQTT_TOPIC" ]; then
  echo "env variable MQTT_BROKER MQTT_TOPIC must be set"
  exit 1
fi

if [ ! -n "$MQTT_PORT" ]; then
  MQTT_PORT=1883
fi

if [ ! -n "$MQTT_KEEPALIVE_INTERVAL" ]; then
  MQTT_KEEPALIVE_INTERVAL=60
fi

if [ ! -n "$PM25_THRESHOLD" ]; then
  PM25_THRESHOLD=71
fi

echo $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_TOPIC_DISPLAY
while true;
do

#main
#get PM2.5 only
#echo "$(python g3.py | awk '{print $2}')"
#get PM1, PM2.5 and PM10
#remove space,[ and ]
#echo "$output$(python g3.py | sed 's/ //g;s/\[//;s/\]//')" > /var/log/pm25_cf.txt && \

# execute g3.py to get pm25 data
pmstr=$(python g3.py | awk '{print $2}')
pm25=${pmstr%","}
echo pm25: $pm25

if [ $pm25 -gt $PM25_THRESHOLD ]; then
  MQTT_MSG=1
else
  MQTT_MSG=0
fi

echo $MQTT_MSG
# publish
if [ ! -n "$MQTT_TOPIC_DISPLAY" ]; then
  python publish.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_MSG
else
  MQTT_MSG_DISPLAY=$pm25
  python publish.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_MSG $MQTT_TOPIC_DISPLAY $MQTT_MSG_DISPLAY
fi

## publish
#python publish.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_MSG

done
