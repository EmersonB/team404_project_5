import paho.mqtt.client as mqtt
import time
'''
py MQTT - https://pypi.python.org/pypi/paho-mqtt/1.1
'''

#Constructor Init
#From https://pypi.python.org/pypi/paho-mqtt/1.1#client

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print "connected ok"
    else:
        print "bad connection Returned code=", rc
    
#
#broker = "192.168.56.1"
broker = "iot.eclipse.org"
client = mqtt.Client("pythonTest") #create new instance
client.on_connect = on_connect  #bind call back function
print "Connecting to broker", broker
client.loop_start()     #start loop
client.connect(broker, 1883)
client.publish("temp","100k")
time.sleep(4)
client.loop_stop()  #
client.disconnect() #disconnect 