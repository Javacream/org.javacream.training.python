import paho.mqtt.client as mqtt
import time

broker = "broker.hivemq.com"
port = 1883
topic = "demo/javacream/chat"

client = mqtt.Client()

client.connect(broker, port)

while True:
    message = input("Enter message to publish: ")
    client.publish(topic, message)
    print(f"Published: {message}")
    time.sleep(1)
