import json
import paho.mqtt.client as mqttClient
import time
from mongoDB_test import get_db
from mongoDB_test import get_collection
from mongoDB_test import insert_into
from pymongo import MongoClient


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")


def write_to_database(payload, db_name, col_name): 
    now = time.time()
    connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
    client = MongoClient(connection_string)
    col = get_collection(db_name,col_name)
    dict_insert = {"weight": float(payload.decode("utf-8")),
                    "time": now,
    }
    db = client["trend_history"]
    col = db["load_values"]
    col.insert_one(dict_insert)

def get_last_Nvalues(n):
    connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
    client = MongoClient(connection_string)
    db = client["trend_history"]
    col = db["load_values"]
    master_list = []
    output_list = []
    for doc in col.find({"weight": {}}).sort("time"):
        master_list.append(doc)
    for i in range(0,n):
        output_list.append(master_list[i])

    return output_list



def on_message(client, userdata, message):
    print("Message received: ")
    print(message.payload.decode("utf-8"))

    write_to_database(message.payload,"trend_history","load_values")

  
Connected = False   #global variable for the state of the connection
  
broker_address= "13.40.33.147"  #Broker address
port = 1883                         #Broker port
user = "myUserAdmin"                    #Connection username
password = "camjfl"            #Connection password
  
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect = on_connect                      #attach function to callback
client.on_message = on_message                      #attach function to callback

client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop

while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("shelf1/weight")
  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()



    

