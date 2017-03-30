#!/bin/sh

#init variable
if [ ! -n "$GPIO_PIN" ]||[ ! -n "$MQTT_BROKER" ]||[ ! -n "$MQTT_TOPIC" ]; then
  echo "env variable GPIO_PIN MQTT_BROKER MQTT_TOPIC must be set"
  exit 1
fi

if [ ! -n "$MQTT_PORT" ]; then
  MQTT_PORT=1883
fi

if [ ! -n "$MQTT_KEEPALIVE_INTERVAL" ]; then
  MQTT_KEEPALIVE_INTERVAL=60
fi

if [ ! -n "$TEMP_THRESHOLD" ]; then
  TEMP_THRESHOLD=40
fi

while true;
do

#main
#get H and T
#echo "$(python dht22.py 22 $GPIO_PIN )"  && \

tempstr=$(python dht22.py 22 $GPIO_PIN | awk -F, '{print $1}')
temp=${tempstr%.*}
echo temperature: $temp

if [ $temp -gt $TEMP_THRESHOLD ]; then
  MQTT_MSG=1
else
  MQTT_MSG=0
fi

# publish
python publish.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_MSG

done
