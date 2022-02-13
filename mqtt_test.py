import paho.mqtt.client as paho
broker = "13.40.33.147"
port = 1883


def on_publish(client,userdata,result):
    """
     create function for callback
    """
    print("data published \n")

def turn_on_led():
    client1= paho.Client("control1")
    client1.username_pw_set(username="myUserAdmin", password="camjfl")   # create client object
    client1.on_publish = on_publish         # assign function to callback
    client1.connect(broker,port)            # establish connection
    ret = client1.publish("shelf1/led","on")       # publish