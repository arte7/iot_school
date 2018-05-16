#!/usr/bin/env python

print("please w8")

import numpy as np
from RPLCD.i2c import CharLCD

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

print("test print")
#GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(SENSOR_PIN, GPIO.IN)

lcd = CharLCD("PCF8574", 0x3f)

def display_humidity():
    print("Fetch temperature and humidity")

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: %d C" % temperature)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: %d %%" % humidity)

    return (humidity, temperature)
print("Temperature: %d C" % temperature)
print("Humidity: %d %%" % humidity)

def toggleLED(channel, onoff):
    GPIO.output(channel, onoff)

def post_data(roomId, accessToken, message, temperature, humidity):
    data = {
        roomId: "Y2lzY29zcGFyazovL3VzL1JPT00vODMzYzhiYTAtNTc1NS0xMWU4LTk\
                1NDMtN2QxYzA5ZTViN2Ux",
        accessToken: "NDNjNTc5NDUtYTNhMy00N2NmLTliOTUtYWFlMmRlYWVmNTlhNm\
                IyOGI2OWUtNjk2",
        message: {
            'temperature': int(temperature),
            'humidity': int(humidity)
        }
    }
    url = 'https://api.ciscospark.com/v1/messages'
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.text)
    print(response.json())
    return response

def callback(channel):
    print("motion detected")
    humidity, temperature = display_humidity()

    post_data(roomId, accessToken, message, temperature, humidity)

    try:
        GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=callback)
        while True:
            time.sleep(0.2)

    except KeyboardInterrupt:
        print("Done...")

    finally:
        GPIO.cleanup()
