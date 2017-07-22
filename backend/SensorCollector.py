import time
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD,ACTION_RELEASED
import sys
sys.path.insert(0, "/home/pi/workspace/iot/Common")
from SensorMsg import SensorMsg

sensor    = SenseHat()
sensorMsg = SensorMsg()
sensorMsg.setDeviceID(102)
sensorMsg.setDeviceLatitude (42.504905)
sensorMsg.setDeviceLongitude(-71.236539)

while True:	
	
	temp = sensor.get_temperature()
	pressure = sensor.get_pressure()
	humidity = sensor.get_humidity()
        orientation = sensor.get_orientation()

	#round to nearest 1/10th
        temp = round (temp, 1)
        pressure =round( pressure, 1)
        humidity = round (humidity, 1)
	#convert temp to fahrenheit
	temp = temp * 1.8 +32

	sensorMsg.setSensorType(1)
	sensorMsg.setSensorValue(temp)
	sensorMsg.updateTime()
	
	msg = sensorMsg.toString()

	sensor.show_message(msg, scroll_speed = 0.05)
	time.sleep(5)

	sensorMsg.setSensorType(2)
        sensorMsg.setSensorValue(pressure)
        sensorMsg.updateTime()

        msg = sensorMsg.toString()

        sensor.show_message(msg, scroll_speed = 0.05)
        time.sleep(5)

	sensorMsg.setSensorType(3)
        sensorMsg.setSensorValue(humidity)
        sensorMsg.updateTime()

        msg = sensorMsg.toString()

        sensor.show_message(msg, scroll_speed = 0.05)
        time.sleep(5)

