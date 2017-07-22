from sense_hat import SenseHat
import sys
import os
import time
import datetime
import random
import json

class SensorWeather():
        device_id = 1
        device_lon = 0.0
        device_lat = 0.0
        device_description = "IoT/Weather"
        device_last_time = time.time()
        device_last_temp = 0.0
        device_last_humidity = 0.0
        device_last_mag = 0.0
        device_last_wind_speed = 0.0
        device_last_rain_gauge = 0.0
        device_last_pressure = 0.0
        device_fixed = True
        device_update_interval = 50000
        device_sensor = SenseHat()

        def _init_(self):
                device_sensor = SenseHat()
                self.device_id = 1
                self.device_lon = random.uniform(-76.8, -77.2)
                self.device_lat = random.uniform(38.75, 39.0)
                self.device_last_time = time.time()
                self.device_last_temp = device_sensor.get_temperature()
                self.device_last_humidity = device_sensor.get_humidity()
                self.device_last_mag = device_sensor.get_compass()
                self.device_last_pressure = device_sensor.get_pressure()
                self.device_last_wind_speed = random.uniform(0.0, 20)
                self.device_last_rain_guage = random.uniform(0.0, 10)
                return self

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

        def update_mag(self):
                device_sensor = SenseHat()
                self.device_last_mag = device_sensor.get_compass()
                self.device_last_time = time.time()

        def update_rain(self):
                self.device_last_rain_guage = 1.63
                self.device_last_time = time.time()

        def update_wind(self):
                self.device_last_wind_speed = random.uniform(0.0, 20)
                self.device_last_time = time.time()

        def update_all(self):
                self.update_temp()
                self.update_humidity()
                self.update_wind()
                self.update_rain()
                self.update_pressure()
                self.update_mag()

        def json_now(self):
                self.update_all()
                dict = {"ID": self.device_id, "Description": self.device_description, "Fixed": self.device_fixed, "Latitude": self.device_lat, "Longitude": self.device_lon, "Time": self.device_last_time, "Info": {"Temperature": self.device_last_temp, "Humidity": self.device_last_humidity, "Pressure": self.device_last_pressure, "Magnetometer": self.device_last_mag, "RainGauge": self.device_last_rain_guage, "WindSpeed": self.device_last_wind_speed}}
                return dict
