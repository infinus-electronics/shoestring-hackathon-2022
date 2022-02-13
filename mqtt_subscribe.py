import json 
from mqtt_test import ret
import paho.mqtt.client as mqttClient
import time


pload_list = []


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
        print("Connection failed")


def on_message(client, userdata, message):
    print("Message received: "  + message.payload)
    if len(pload_list) > 20000:
        del pload_list[0]
        pload_list.append(message.payload)
    else: 
        pload_list.append(message.payload)

Connected = False   #global variable for the state of the connection
  
broker_address= "13.40.33.147"  #Broker address
port = 1883                         #Broker port
user = "myUserAdmin"                    #Connection username
password = "camjfl"            #Connection password
  
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
  
client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("shaft1/weight")
  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()


def return_pload_list():
    return pload_list

