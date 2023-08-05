import paho.mqtt.client as mqtt

# Connecting to the Broker which is hosted in virtual machine

MQTT_BROKER_HOST = 'broker.hivemq.com'
MQTT_BROKER_PORT = 1883
MQTT_KEEP_ALIVE_INTERVAL = 60

# Function to run on connecting to the broker

def on_connect(client, userdata, flags, rc):
    if(rc == 0):
        print(f"Connected successfully with {rc} code and qos {userdata}")
        print("\n\n MQTT Service \n\n")
        client.subscribe("House/Living/Light    ") # subscribing to a topic
        client.subscribe("House/Living/Thermostat") 
    else:
        print("Error")

# Function to be invoked on recieving a message

def on_message(client, userdata, message):
    print("Message topic = ",message.topic,"\t Message received = " ,str(message.payload.decode("utf-8"))+"\n")

# Instantiating a client

client = mqtt.Client(transport="tcp",reconnect_on_failure="true")

client.connect_async(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_KEEP_ALIVE_INTERVAL)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
