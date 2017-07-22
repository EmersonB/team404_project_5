import time
import datetime

class SensorMsg(object):
	def _init_(self):
		self.device_id     = None
		self.device_status = 0
		self.device_lat    = 0.0
		self.device_lon    = 0.0
		self.device_type   = 0 
		self.device_val    = 0.0
		self.time_stamp    = time.time()
		self.time_str      = none
	
	def getDeviceID(self):
		return self.device_id
	def setDeviceID (self, deviceID):
		self.device_id = deviceID

	def getDeviceStatus(self):
		return self.device_status
	def setDeviceStatus(self,deviceStatus):
		self.device_status = deviceStatus

	def getDeviceLatitude(self):
		return self.device_lat
	def setDeviceLatitude(self,deviceLat):
		self.device_lat = deviceLat

	def getDeviceLongitude(self):
		return self.device_lat
	def setDeviceLongitude (self, deviceLon):
		self.device_lon = deviceLon

	def getSensorType(self):
		return self.sensor_type
	def setSensorType(self, sensorType):
		self.sensor_type = sensorType

	def getSensorValue (self):
		return self.sensor_val
	def setSensorValue (self, sensorVal):
		self.sensor_val = sensorVal

	def getTimeStamp (self):
		return self.time_stamp
	def setTimeStamp (self, timeStamp):
		self.time_stamp = timeStamp
	def updateTime(self):
	#	self.time_str = str(self.time_stamp)

	def parseMessage (self, msg):
		kvpTokens = msg.split(';')
		for kvp in kvpTokens:
			kvpArray = kvp.split('=')
			key	 = kvpArray[0]
			val      = kvpArray[1]
			if key == "deviceID":
				self.device_id = val
			if key == "deviceStatus":
				self.device_status = int (val)
			if key == "deviceLat":
				self.device_lat = float(val)
			if key == "deviceLon":
				self.device_lon = float (val)
			if key == "sensorType":
				self.sensor_type = int(val)
			if key == "sensorVal":
				self.sensor_val = float(val)
			if key == "timeStamp":
				self.time_stamp = float(val)
	def toString(self):
		self.time_str = datetime.datetime.fromtimestamp(self.time_stamp).strftime ('%Y-%m-%dZ%H:%S')
		msg = "deviceID=%s; deviceStatus=%s; deviceLat=%s; deviceLon=%s; timeStamp=%s; sensorType=%s; sensorVal= %s" % (self.device_id, self.device_status, self.device_lat, self.device_lon, self.time_stamp, self.sensor_type, self.sensor_val)
		return msg
	def _str_(self):
		return self.toString()
