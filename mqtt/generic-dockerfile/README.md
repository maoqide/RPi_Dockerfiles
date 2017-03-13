# mqtt generic-dockerfile

## Introduction
an generic image using mqtt for raspberry pi. 

### requirements
- raspberry pi with docker installed.
- mqtt broker(mosquitto)
- active sensors
- passive sensors

### what can do
you can start multi active sensors, and if any one of them publish SIGNAL_DO to a topic, the passive sensor subscribed to the same topic will DO.

## active
active sensors like pir/light sensor/voice sensor...    
it can output 0/1 as result.

### command
```shell
# run
docker run -d --privileged --env GPIO_PIN=17 --env MQTT_BROKER=192.168.10.245 --env MQTT_PORT=1883 --env MQTT_KEEPALIVE_INTERVAL=60 --env MQTT_TOPIC='test/light' --env SIGNAL_DO=1 --name test_light maoqide/rpi-mqtt-publisher
```

### explanation
| env varibles | required | description | more |
| ------ | ------ | ------ | ------ |
| GPIO_PIN | true | GPIO num |  |
| MQTT_BROKER | true | ip/addr of mqtt broker |  |
| MQTT_PORT | false | port of mqtt broker | default 1883 |
| MQTT_KEEPALIVE_INTERVAL | false |  | default 60 |
| MQTT_TOPIC | true | topic to publish | format like 'prefix/topic' is recommended,and 'prefix/#' to publish to multi topic that has the same prefix. |
| SIGNAL_DO | false | 0/1 | default 1, represent for publish message '1' to let passive sensor subscribed to the same topic do sth. '0' the opposite. |


## passive
passive sensors like led/buzzer...    
you can input 0/1 to control it.

### command
```shell
# run
docker run -d --privileged --env GPIO_PIN=20 --env MQTT_BROKER=192.168.10.245 --env MQTT_TOPIC='test/#' maoqide/rpi-mqtt-subscriber
```

### explanation
| env varibles | required | description | more |
| ------ | ------ | ------ | ------ |
| GPIO_PIN | true | GPIO num |  |
| MQTT_BROKER | true | ip/addr of mqtt broker |  |
| MQTT_PORT | false | port of mqtt broker | default 1883 |
| MQTT_KEEPALIVE_INTERVAL | false |  | default 60 |
| MQTT_TOPIC | true | topic to subscribe | format like 'prefix/topic' is recommended,and 'prefix/#' to subscribe to multi topic that has the same prefix. |
