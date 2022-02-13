"""
Check weight increase by querying MongoDB
Publish to MQTT broker to turn LED on
To be run indefinitely
"""

import paho.mqtt.client as paho
import pymongo
from pymongo import MongoClient
import smtplib
import time

broker = "13.40.33.147"
port = 1883

email_last_sent = time.time()
neversent =1

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


while True:
    data_list = get_last_Nvalues(5)
    print(data_list)
    # Weight increase
    if (data_list[0] - ave_of_list(data_list[1:])) > 200:
        turn_on_led()
    # Low level alert
    if ave_of_list(data_list) < 300 and mid_of_list(data_list) < 300:
        if time.time() - email_last_sent > 20:
            send_email("Weight is below 300g. Please restock")
            print("Email was sent")
            email_last_sent = time.time()
            neversent=0
