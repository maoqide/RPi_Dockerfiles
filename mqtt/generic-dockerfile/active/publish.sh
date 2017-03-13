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

if [ ! -n "$SIGNAL_DO" ]; then
  SIGNAL_DO=1
fi

echo $GPIO_PIN $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $SIGNAL_DO

#loop
while true
do
	#python publish.py 17 192.168.10.245 1883 30 test/light 1
	python publish.py $GPIO_PIN $MQTT_BROKER $MQTT_PORT $MQTT_KEEPALIVE_INTERVAL $MQTT_TOPIC $SIGNAL_DO
done
