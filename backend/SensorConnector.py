from sense_hat import SenseHat
import paho.mqtt.client as paho
import os
import socket
import ssl
import json
import time
from time import sleep
import random
from SensorEarthquake import SensorEarthquake

connFlag = False


def gen_message(dict_obj):
        json_file = json.dumps(dict_obj, indent=2)
        return json_file

def on_connect(client, userdata, flags, rc):
        global connflag
        connflag = True
        print("Connection returned result: " + str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def connect(sensor):
        mqttc = paho.Client()
        mqttc.on_connect = on_connect
        mqttc.on_message = on_message

        awshost = 'a2xny3fbaa9vhr.iot.us-east-1.amazonaws.com'
        awsport = 8883
        clientId = "myThingName"
        thingName = "thing_pi"
        caPath = "./aws_key.crt"
        certPath = "../custom_cert/4d08b0576f-certificate.pem.crt"
        keyPath = "../custom_cert/4d08b0576f-private.pem.key"
        print(certPath, keyPath)
        mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

        mqttc.connect(awshost, awsport, keepalive=3)

        mqttc.loop_start()


        mqttc02 = paho.Client()
        mqttc02.on_connect = on_connect
        mqttc02.on_message = on_message
        #mqttc02.on_log = on_log

        awshost = '10.5.6.162'
        awsport = 8883

        mqttc02.connect(awshost, awsport, keepalive=3)

        mqttc02.loop_start()

        i=0
        while i<100:
                sleep(0.5)
                if connflag:
                        sensor.update_all()
                        dict = sensor.json_now()
                        json_file = gen_message(dict)
                        mqttc.publish(dict['Description'], json_file, qos=1)
                        mqttc02.publish("iot", json_file, qos=1)
                else:
                        print("waiting for connection...")
                i=i+1


sensor = SensorEarthquake()._init_()
connect(sensor)
