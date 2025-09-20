
import paho.mqtt.client as mqtt

broker_ip = 'localhost'
file = open('logs')
def parseResponseMoney(data):
    data_list = data.split('\n').slice(',')
    timestamp = data_list[0]
    money = data_list[1]
    return (timestamp,money)

def on_message_recieve(client, userdata, message):
    if message.topic == "smart-garden/Temperature":
        print(f"TEMP: {message.payload.decode()}")
    elif message.topic == "smart-garden/Fire":    
        print(f"Fire: {message.payload.decode()}")
    elif message.topic == "smart-garden/Capacity":    
        print(f"Capacity: {message.payload.decode()}")
    elif message.topic == "smart-garden/Money":
        parseResponseMoney(message.payload.decode())    
        print(f"Money: {message.payload.decode()}")

client = mqtt.Client(client_id="Main-Server")

client.connect(broker_ip,1883)

client.subscribe("smart-garden/Temperature")
client.subscribe("smart-garden/Fire")
client.subscribe("smart-garden/Capacity")
client.subscribe("smart-garden/Money")

client.on_message = on_message_recieve

client.loop_forever()