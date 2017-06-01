#!/bin/sh

#init variable
if [ ! -n "$GPIO_PIN_TRIG" ]||[ ! -n "$GPIO_PIN_ECHO" ]||[ ! -n "$MQTT_BROKER" ]||[ ! -n "$MQTT_TOPIC" ]; then
  echo "env variable GPIO_PIN_TRIG GPIO_PIN_ECHO MQTT_BROKER MQTT_TOPIC must be set"
  exit 1
fi

if [ ! -n "$MQTT_PORT" ]; then
  MQTT_PORT=1883
fi

if [ ! -n "$MQTT_KEEPALIVE_INTERVAL" ]; then
  MQTT_KEEPALIVE_INTERVAL=60
fi

if [ ! -n "$DIST_THRESHOLD" ]; then
  DIST_THRESHOLD=20
fi

if [ ! -n "$INTERVAL" ]; then
  INTERVAL=1
fi

echo $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_TOPIC_DISPLAY
while true;
do

#main

dist=$(python hc_sr04.py $GPIO_PIN_TRIG $GPIO_PIN_ECHO)
distance=${dist%.*}
echo $distance

if [ $distance -lt $DIST_THRESHOLD ]; then
  MQTT_MSG=1
else
  MQTT_MSG=0
fi

echo $MQTT_MSG
# publish
if [ ! -n "$MQTT_TOPIC_DISPLAY" ]; then
  python publish.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_MSG
else
  MQTT_MSG_DISPLAY=$distance
  python publish.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $MQTT_MSG $MQTT_TOPIC_DISPLAY $MQTT_MSG_DISPLAY
fi

sleep $INTERVAL

done
