import paho.mqtt.client as mqtt
import random
import time

client = mqtt.Client(transport="tcp")
client.connect("broker.hivemq.com",1883,60)

switch = ["ON","OFF"]
i = random.randint(10,30)
client.publish("House/Living/Thermostat",i)
client.publish("House/Living/Light    ",random.choice(switch))
client.publish("House/Room/Fan",random.choice(switch))
time.sleep(2)