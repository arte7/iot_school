#!/usr/bin/env python

print("please w8")

import numpy as np
from RPLCD.i2d import CharLCD

import RPi.GPIO as GPIO
import time
import os
import json
import requests

GPIO.setmode(GPIO.BCM)

import sys
import Adafruit_DHT

TRIG = 23
ECHO = 24
SENSOR_PIN = 12

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SENSOR_PIN, GPIO.IN)

lcd = CharLCD("PCF8574", 0x3f)

def display_humidity():
    print("Fetch temperature and humidity")

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    lcd.cursor.pos = (0, 0)
    lcd.write_string("Temp: %d C" % temperature)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: %d %%" % humidity)

    print ("Temperature: %d C" % temperature)
    print("Humidity: %d %%" % humidity)
    return (humidity, temperature)

def post_data(temerature, humidity):
    data = {
        'measurements': {
            'temperature': int(temperature),
            'humidity': int(humidity)
        }
    }
    url = #look up spark api
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.text)
    print(response.json())
    return response

def callback(channel):
    print("motion detected")
    humidity, temperature = display_humidity()

    post_data(temperature, humidity)

    try:
        GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=callback)
        while True:
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("Done...")

    finally:
        GPIO.cleanup()
