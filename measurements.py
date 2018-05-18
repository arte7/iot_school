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

sensor = Adafruit_DHT.DHT11
pin = 4
accessToken = "accessToken"

roomId = "roomId"

GPIO.setup(SENSOR_PIN, GPIO.IN)

lcd = CharLCD("PCF8574", 0x3f)

def display_humidity():
    print("Fetch Temperature and Humidity")
    sensor = Adafruit_DHT.DHT11
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    lcd.cursor_pos = (0, 0)
    lcd.write_string("Temp: %d C" % temperature)
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Humidity: %d %%" % humidity)

    print("Temperature: %d C" % temperature)
    print("Humidity: %d %%" % humidity)

    return (humidity, temperature)

def toggleLED(channel, onoff):
    GPIO.output(channel, onoff)

def post_data(roomId, accessToken, temperature, humidity):
    data = {
        'roomId': str(roomId),
        'accessToken': str(accessToken),
        'text': '{"Temperature": '+str(temperature)+', "Humidity": '+str(humidity)+'}'
    }
    url = 'https://api.ciscospark.com/v1/messages'
    headers = {"Authorization":"Bearer " + accessToken,
        "Content-Type":"application/json; charset=utf-8"}
    response = requests.post(url, headers=headers, verify=True, json=data)
    print(response.status_code)
    print(response.text)
    print(response.json())
    return response

def callback(channel):
    print("motion detected")
    humidity, temperature = display_humidity()

    post_data(roomId, accessToken, temperature, humidity)

try:
    GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=callback)
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print("Done...")

finally:
    GPIO.cleanup()
