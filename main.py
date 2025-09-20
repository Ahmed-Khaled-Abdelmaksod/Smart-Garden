import RPi.GPIO as GPIO
import time
from gpiozero  import LED,DistanceSensor
import math
import random
import paho.mqtt.client as mqtt

#from DIYables_MicroPython_LCD_I2C import LCD_I2C
#from machine import I2C,Pin

#rtc_sda = Pin(2)
#rtc_scl = Pin(3)
broker_ip = '192.168.137.178'
client = mqtt.Client("Smart-Garden")
client.connect(broker_ip,1883)

enter_ultra = DistanceSensor(echo=14,trigger=15)
outer_ultra = DistanceSensor(echo=18,trigger=23)


LCD_ADDR = 39

capacity_red_led = LED(24)
capacity_green_led = LED(25)


post_leds = LED(17)
fan_sig = LED(27)
ldr = 0

#from RPLCD.i2c import CharLCD

# Adjust address if your LCD is at 0x3F
#lcd = CharLCD('PCF8574', 0x27,cols=16,rows=2)

#lcd.write_string("HelLo AAA")

entering_distance = 0
outing_distance = 0

people_max_capacity = 10

adult_ticket = 10
child_ticket = 5
money = 0.0
people_inside = 0

def get_ultras_distance():
    
    entering_distance = (enter_ultra.distance * 100)
    outing_distance = outer_ultra.distance * 100
    print("ENter Dis:" + str(entering_distance))
    print("OUter Dis:" + str(outing_distance))
    return (entering_distance,outing_distance)
while True:
    client.publish("smart-garden/Money",f"{timestamp},{money}")
    ldr = random.randint(50,90)
    dht = random.randint(18,35)
    entering_distance , outing_distance = get_ultras_distance()
    if entering_distance < 8 and people_inside < people_max_capacity:
       people_inside += 1
       money += child_ticket
       timestamp = time.time()
       print("Money : "+str(money))

    elif entering_distance < 15 and people_inside < people_max_capacity:
       people_inside += 1
       money += adult_ticket
       print("Money : "+str(money))

    if outing_distance < 15 and people_inside != 0:
       people_inside -= 1

    if people_inside < people_max_capacity :
       capacity_green_led.on()
       capacity_red_led.off()
    else:
       capacity_red_led.on()
       capacity_green_led.off()
    print(ldr)
    if ldr > 70:
        post_leds.on()
    else:
        post_leds.off()

    print(people_inside)
    if dht > 25:
       fan_sig.on()
    else:
       fan_sig.off()
    time.sleep(0.6)
