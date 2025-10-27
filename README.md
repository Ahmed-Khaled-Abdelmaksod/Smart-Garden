# Smart Garden System

An IoT-based system designed to automate and monitor garden environments using real-time sensor data.  
The system tracks temperature, humidity, light intensity, crowd capacity, and fire detection, enabling smart control and data visualization through the **Blynk IoT platform**.

---

## Team Members
- **Amr Saad**
- **Ahmed Kandil**  
- **Ahmed Khaled** 

---

## Problem Statement
The project aims to digitalize traditional gardens by creating a **smart, automated environment** capable of monitoring environmental conditions, ensuring safety, and enabling data-driven control.

---

## Solution Overview
The **Smart Garden System** utilizes a Raspberry Pi connected to sensors and actuators to collect data such as temperature, humidity, light intensity, and occupancy.  
This data is published through **MQTT** and **HTTP** protocols and displayed on the **Blynk IoT Dashboard** for real-time monitoring and automation.

---

## Features
- **Environmental Monitoring:** Tracks temperature, humidity, light intensity, and fire detection in real time.  
- **Smart Automation:** Controls lights, fans, and pumps based on environmental thresholds.  
- **Crowd Management:** Uses an ultrasonic sensor to detect the number of visitors entering and exiting the garden.  
- **Alert System:** Triggers a buzzer and LED indicators during unsafe or fire conditions.
- **Smart Notifications:** Sends instant alerts to **Telegram** and **E-mail** when fire or unsafe conditions are detected.
- **IoT Integration:** Uses **Blynk** and **Node-RED** for remote data visualization and control.
---

## Communication Protocols

### MQTT
Used for real-time communication between devices and the Raspberry Pi.  
**Topics:**
- `temperature`: Transmits current temperature readings.  
- `money`: Tracks revenue collected in real time.  
- `capacity`: Monitors current visitor count.  
- `fire`: Indicates fire or smoke status.  

### HTTP
Used for sending collected sensor data to the **Blynk Dashboard** for live monitoring and control.

---

## IoT Platform Integration (Blynk)
1. Created a project template and added a new device on the Blynk platform.  
2. Configured data streams for each MQTT topic (temperature, money, capacity, fire).  
3. Designed a user-friendly dashboard with labeled widgets.  
4. Integrated the **Blynk authentication token** and defined **virtual pins** for each stream.  
5. Linked real-time data from Raspberry Pi to the dashboard for visualization and control.

---

## Hardware Components

### Sensors
| Sensor | Function |
|---------|-----------|
| DHT22 | Measures temperature and humidity |
| LDR | Detects light intensity (day/night) |
| Ultrasonic Sensor | Detects number of people entering/exiting |
| Smoke Sensor | Detects smoke or fire |

### Actuators
| Actuator | Function |
|-----------|-----------|
| LEDs | Indicate sensor and system status |
| Buzzer | Alerts in case of smoke/fire detection |
| Fans & Water Pumps | Automatically activated when temperature exceeds limit |

---

## System Workflow
1. Sensors collect environmental data from the garden.  
2. The Raspberry Pi processes and transmits this data using MQTT.  
3. The Blynk Dashboard receives and visualizes live readings.  
4. Actuators respond automatically to environmental conditions.  
5. Alerts and updates are reflected instantly on the dashboard.

---

## Conclusion
The **Smart Garden System** demonstrates how IoT technologies can be applied to build **sustainable and intelligent environments**.  
By combining automation, real-time monitoring, and cloud integration, the project illustrates the impact of IoT in advancing digital transformation and smart living.

---

## Acknowledgment
This project was developed as part of the **Samsung Innovation Campus (SIC) – IoT Track**, organized by **Samsung Electronics** in collaboration with the **Life Makers Foundation Egypt**.  
