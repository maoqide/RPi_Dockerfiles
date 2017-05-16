#!/bin/sh

#init variable
#if [ ! -n "$MQTT_BROKER" ]||[ ! -n "$MQTT_TOPIC" ]; then
#  echo "env variable MQTT_BROKER MQTT_TOPIC must be set"
#  exit 1
#fi

if [ ! -n "$MQTT_PORT" ]; then
  MQTT_PORT=1883
fi

if [ ! -n "$MQTT_KEEPALIVE_INTERVAL" ]; then
  MQTT_KEEPALIVE_INTERVAL=60
fi

echo $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC


python control.py 192.168.10.245 1883 30 'test/#'
#python control.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC

