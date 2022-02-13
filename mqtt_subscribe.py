import json
import paho.mqtt.client as mqttClient
import time
import datetime 
from mongoDB_test import get_db
from mongoDB_test import get_collection
from mongoDB_test import insert_into

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")

def write_to_database(payload, db_name, col_name): 
    now = datetime.now()
    col = get_collection(db_name,col_name)
    dict_insert = {"weight" : payload,
                    "time" : now.strftime("%m/%d/%Y %H:%M:%S")
    }
    insert_into(col,dict_insert)

def on_message(client, userdata, message):
    print("Message received: "  + message.payload)
    write_to_database(message.payload,"trend_history","load_values")

  
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



    

