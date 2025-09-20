import paho.mqtt.client as mqtt

broker_ip = '192.168.137.178'

client = mqtt.Client("Smart-Garden")

client.connect(broker_ip,1883)

client.publish("smart-garden/Temperature","Ahmed")

client.disconnect()