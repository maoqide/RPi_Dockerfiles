#!/bin/sh

if [ ! -n "$FLOW_MIN" ]; then
  FLOW_MIN=30
fi

#main
python auto-water.py $GPIO_FLOW $GPIO_SOIL $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $FLOW_MIN

