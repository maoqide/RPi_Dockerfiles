# sensors
- water flow(YF-S401)
- soil humidity(YL-69)
- water pump
- relay

# requirement
- MQTT broker(like mosquitto) started.
- docker-compose.yaml modified.

# required docker images
- localtest/mqtt-auto-watering
- localtest/rpi-mqtt-subscriber

# env description

followings are environment in docker-compose.yaml, should modify them to proper value before start it.
 
| env         | description    |
| :---:       | :------------: |
| MQTT_BROKER | ip of where MQTT broker(like mosquitto) started |
| MQTT_PORT   | port MQTT broker listened, default 1883 |
| MQTT_KEEPALIVE_INTERVAL | interval for a MQTT connection |
| MQTT_TOPIC | MQTT topic that a sensor subscribed or published |
| GPIO_FLOW | water flow sensor GPIO pin |
| GPIO_SOIL | soil humidity sensor GPIO pin |
| FLOW_MIN | the minimum value of the flow(ml/s), below which the pump would stop |

# start
```bash
cd mqtt-packages/auto-watering
sudo make up
```
