#!/usr/bin/python

# this source is part of my Hackster.io project:  https://www.hackster.io/mariocannistra/radio-astronomy-with-rtl-sdr-raspberrypi-and-amazon-aws-iot-45b617

# use this program to test the AWS IoT certificates received by the author
# to participate to the spectrogram sharing initiative on AWS cloud

# this program will publish test mqtt messages using the AWS IoT hub
# to test this program you have to run first its companion awsiotsub.py
# that will subscribe and show all the messages sent by this program

import paho.mqtt.client as paho
import os
import socket
import ssl
import json
from time import sleep
from random import uniform, random

connflag = False

def gen_message(dict_obj):
    '''
    Generate JSON file
    '''
    json_file = json.dumps( dict_obj, indent=2, sort_keys=True)
    return json_file


def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

#def on_log(client, userdata, level, buf):
#    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
#mqttc.on_log = on_log

awshost = 'a2xny3fbaa9vhr.iot.us-east-1.amazonaws.com'
awsport = 8883
clientId = "myThingName"
thingName = "thing_pi"
caPath = ".\\aws_key.crt"
certPath = ".\\custom_cert\\4d08b0576f-certificate.pem.crt"
keyPath = ".\\custom_cert\\4d08b0576f-private.pem.key"
print certPath, keyPath
mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=3)

mqttc.loop_start()
i=0
while i<10:
    sleep(0.5)
    device_dict = {}
    if connflag == True:
        tempreading = uniform(20.0,25.0)
        humreading = random()
        device_dict['temp'] = tempreading
        device_dict['humidity'] = humreading
        json_file = gen_message(device_dict)
        mqttc.publish("temperature", json_file, qos=1)
        print("msg sent: temperature " + "%.2f" % tempreading )
    else:
        print("waiting for connection...")
    i=i+1