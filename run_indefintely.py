import json
import paho.mqtt.client as mqttClient
import time
from mongoDB_test import get_db
from mongoDB_test import get_collection
from mongoDB_test import insert_into
from pymongo import MongoClient



import paho.mqtt.client as paho
import pymongo
from pymongo import MongoClient
import smtplib
import time

broker = "13.40.33.147"
port = 1883

email_last_sent = time.time()

def get_last_Nvalues(n):
    connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
    client = MongoClient(connection_string)
    db = client["trend_history"]
    col = db["load_values"]
    output_list = []
    for i, doc in enumerate(col.find().sort("time", pymongo.DESCENDING)):
        output_list.append(doc['weight'])
        if i == n-1:
            break
    return output_list


def on_publish(client,userdata,result):
    """
     create function for callback
    """
    print("Publish to MQTT broker to turn on LED \n")


def turn_on_led():
    client1 = paho.Client("control8")
    client1.username_pw_set(username="myUserAdmin", password="camjfl")   # create client object
    client1.on_publish = on_publish         # assign function to callback
    client1.connect(broker,port)            # establish connection
    ret = client1.publish("shelf1/led","on")       # publish


def send_email(msg, listofemails="cosana4309@diolang.com"):
    """
    Args:
        msg: A string to be included in the content of the email
        listofemails: like ['hidevix479@diolang.com', "ten28@cam.ac.uk"]
    """

    gmail_user = 'duriancendoljfl@gmail.com'
    gmail_password = 'ifmhackathon'
    listofemails = ["cosana4309@diolang.com"]

    sent_from = gmail_user
    to = listofemails
    subject = "Low Stock Alert"
    body = msg

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….email was not sent",ex)


def ave_of_list(lst):
    """
    Returns the average of the values in the list
    """
    total = 0
    for i in lst:
        total += i
    return total * 1.0 / len(lst)


def mid_of_list(lst):
    """
    Returns the median of the list
    """
    lst.sort()
    return lst[len(lst)//2]

connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
client = MongoClient(connection_string)






def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected  # Use global variable
        Connected = True  # Signal connection
    else:
        print("Connection failed")


def write_to_database(payload, db_name, col_name):
    now = time.time()
    connection_string = "mongodb://myUserAdmin:camjfl@13.40.33.147"
    client = MongoClient(connection_string)
    col = get_collection(db_name, col_name)
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
    for i in range(0, n):
        output_list.append(master_list[i])
    print(output_list)
    return output_list


def on_message(client, userdata, message):
    print("Message received: ")
    print(message.payload.decode("utf-8"))

    write_to_database(message.payload, "trend_history", "load_values")


Connected = False  # global variable for the state of the connection

broker_address = "13.40.33.147"  # Broker address
port = 1883  # Broker port
user = "myUserAdmin"  # Connection username
password = "camjfl"  # Connection password

client = mqttClient.Client("Python")  # create new instance
client.username_pw_set(user, password=password)  # set username and password
client.on_connect = on_connect  # attach function to callback
client.on_message = on_message  # attach function to callback

client.connect(broker_address, port=port)  # connect to broker

client.loop_start()  # start the loop

while Connected != True:  # Wait for connection
    time.sleep(0.1)

client.subscribe("shelf1/weight")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()





