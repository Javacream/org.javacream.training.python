import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "demo/javacream/chat"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(f"Received: {msg.payload.decode()} on topic {msg.topic}")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)
client.loop_forever()
