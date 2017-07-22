import paho.mqtt.client as mqtt
import time

'''
This may not work,  I am copying this by hand right now
'''

broker = "iot.eclipse.org"  #Our MQTT Broker, will be amazon rest API
client = mqtt.Client("pythonTest")
client.on_connect = on_connect
print "Connecting to broker", broker
client.loop_start()
client.conect(broker, 1883)
client.publish("temp", "100K") #(stream, value)
time.sleep(4)
client.loop_stop()
client.disconnect() #Disconnect
