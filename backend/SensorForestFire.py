
from sense_hat import SenseHat
import sys
import os
import time
import datetime
import random
import json

class SensorForestFire():
        device_id = None
        device_lon = 0.0
        device_lat = 0.0
        device_description = "ForestFire"
        device_last_time = time.time()
        device_last_temp = 0.0
        device_last_humidity = 0.0
        device_last_pressure = 0.0
        device_last_accel = 0.0
        device_fixed = True
        device_update_interval = 50000
        device_sensor = SenseHat()

        def _init_(self):
                self.device_id = random.random()
                self.device_lon = random.uniform(-76.8, -77.2)
                self.device_lat = random.uniform(38.75, 39.0)
                self.device_last_time = time.time()
                self.device_last_temp = device_sensor.get_temperature()
                self.device_last_humidity = device_sensor.get_humidity()
                self.device_last_accel = get_accelerometer()
                self.device_last_pressure = get_pressure()

        def update_temp(self):
                device_sensor = SenseHat()
                self.device_last_temp = device_sensor.get_temperature()
                self.device_last_time = time.time()
                return self.device_last_temp

        def update_humidity(self):
                device_sensor = SenseHat()
                self.device_last_humidity = device_sensor.get_humidity()
                self.device_last_time = time.time()

        def update_pressure(self):
                device_sensor = SenseHat()
                self.device_last_pressure = device_sensor.get_pressure()
                self.device_last_time = time.time()

        def update_accel(self):
                device_sensor = SenseHat()
                self.device_last_accel = device_sensor.get_accelerometer()
                self.device_last_time = time.time()

        def update_all(self):
                self.update_temp()
                self.update_humidity()
                self.update_pressure()
                self.update_accel()

        def json_now(self):
                self.update_all()
                dict = {"ID": self.device_id, "Description": self.device_description, "Fixed": self.device_fixed, "Latitude": self.device_lat, "Longitude": self.device_lon, "Time": self.device_last_time, "Info": {"Temperature": self.device_last_temp, "Humidity": self.device_last_humidity, "Pressure": self.device_last_pressure, "Accelerometer": self.device_last_accel}}
                return dict
