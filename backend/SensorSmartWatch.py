
from sense_hat import SenseHat
import sys
import os
import time
import datetime
import random
import json

class SensorSmartWatch():
        device_id = 4
        device_lon = 0.0
        device_lat = 0.0
        device_description = "IoT/SmartWatch"
        device_last_time = time.time()
        device_last_accel = 0.0
        device_last_gyro = 0.0
        device_last_mag = 0.0
        device_fixed = False
        device_update_interval = 50000
        device_sensor = SenseHat()

        def _init_(self):
                device_sensor = SenseHat()
                self.device_id = 4
                self.device_lon = random.uniform(-76.8, -77.2)
                self.device_lat = random.uniform(38.75, 39.0)
                self.device_last_time = time.time()
                self.device_last_temp = device_sensor.get_gyroscope()
                self.device_last_humidity = device_sensor.get_accelerometer()
                self.device_last_mag = device_sensor.get_compass()
                self.device_last_pressure = device_sensor.get_pressure()
                return self

        def update_accel(self):
                device_sensor = SenseHat()
                self.device_last_temp = device_sensor.get_accelerometer()
                self.device_last_time = time.time()

        def update_gyro(self):
                device_sensor = SenseHat()
                self.device_last_humidity = device_sensor.get_gyroscope()
                self.device_last_time = time.time()

        def update_mag(self):
                device_sensor = SenseHat()
                self.device_last_mag = device_sensor.get_compass()
                self.device_last_time = time.time()

        def update_location(self):
                self.device_lon = self.device_lon + random.uniform(-0.0002, 0.0002)
                self.device_lat = self.device_lat + random.uniform(-0.0002, 0.0002)


        def update_all(self):
                self.update_gyro()
                self.update_accel()
                self.update_mag()
                self.update_location()

        def json_now(self):
                self.update_all()
                dict = {"ID": self.device_id, "Description": self.device_description, "Fixed": self.device_fixed, "Latitude": self.device_lat, "Longitude": self.device_lon, "Time": self.device_last_time, "Info": {"Acceleration": self.device_last_accel, "Gyroscope": self.device_last_gyro, "Magnetometer": self.device_last_mag}}
                return dict
