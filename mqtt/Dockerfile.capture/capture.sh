#!/bin/sh

#init variable
if [ ! -n "$MQTT_BROKER" ]||[ ! -n "$MQTT_TOPIC" ]; then
  echo "env variable MQTT_BROKER MQTT_TOPIC must be set"
  exit 1
fi

echo $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC

#python capture.py 192.168.10.245 1883 30 'test/#'
python capture.py $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC
