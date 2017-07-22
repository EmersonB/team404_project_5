from sense_hat import SenseHat
import sys
sensor = SenseHat()

sys.path.insert(0, "/home/pi/workspace/iot/Common")
from SensorMsg import SensorMsg
sensorMsg = SensorMsg()
sensorMsg.setDeviceID(101)
sensorMsg.setDeviceLatitude (12.34567)
sensorMsg.setDeviceLongitude(-123.4567)

while True:
	temp = sensor.get_temperature()
	pressure = sensor.get_pressure()
	humidity = sensor.get_humidity()

	sensorMsg.setSensorType(1)
	sensorMsg.setSensorValue(temp)
	sensorMsg.updateTime()
	
	msg = sensorMsg.toString()

	sensor.show_message(msg, scroll_speed = 0.10)
	time.sleep(5)

	
	#round to nearest 1/10th
	temp = round (temp, 1)
	pressure =round( pressure, 1)
	humidity = round (humidity, 1)
	# create message
	msg = "Temp=%s, Pressure= %s, Humidity = %s" %(temp, pressure, humidity) 
	#speed in secs
	sensor.show_message(msg, scroll_speed = 0.05)

	time.sleep(5)
