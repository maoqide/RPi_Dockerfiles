# requirement
- MQTT broker(like mosquitto) started.

- docker images localtest/rpi-mqtt-hcsr04、localtest/rpi-moto built.
- docker-compose.yaml modified.

# build image
```bash
cd mqtt-packages/moto
sudo make build
```

# env description

followings are environment in docker-compose.yaml, should modify them to proper value before start it.
 
| env         | description    |
| :---:       | :------------: |
| MQTT_BROKER | ip of where MQTT broker(like mosquitto) started |
| MQTT_PORT   | port MQTT broker listened, default 1883 |
| MQTT_KEEPALIVE_INTERVAL | interval for a MQTT connection |
| MQTT_TOPIC | MQTT topic that a sensor subscribed or published |
| INTERVAL | the interval between the sensor publish a message |
| GPIO_PIN_TRIG | HC-SR04 TRIG pin |
| GPIO_PIN_ECHO | HC-SR04 ECHO pin |
| DIST_THRESHOLD | distance threshold, below which the camera will do capturing and ocr |

# start
```bash
cd mqtt-packages/moto
sudo make up
```
