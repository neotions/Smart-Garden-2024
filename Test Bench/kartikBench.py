# Imports
import requests
import RPi.GPIO as GPIO
import time

from helperFunctons import *

# Test Bench class
class TestBench:

    def __init__(self,pins):
        self.moisturePin = pins['moisture']
        self.lightPin = pins['light']
        # Set up GPIO mode
        GPIO.setmode(GPIO.BCM)

        # Set up GPIO pin for sensor input
        sensor_pin = 17
        GPIO.setup(sensor_pin, GPIO.IN)
    
    # Returns the moisture sensor data
    def getMoisture(self):
        try:
            sensor_data = GPIO.input(self.moisturePin)
        except Exception as e:
            betterPrint(f"Error reading data from moisture sensor on pin {self.moisturePin}: {e}", "red")
        return sensor_data
    
    # Returns the light sensor data
    def getLight(self):
        try:
            sensor_data = GPIO.input(self.lightPin)
        except Exception as e:
            betterPrint(f"Error reading data from light sensor on pin {self.lightPin}: {e}", "red")
        return sensor_data
    
    # WIP DO NOT USE
    def serverPost(self,data):
        response = requests.post('http://smart-farm.xyz/', json=data)
        return response
    
    # WIP DO NOT USE
    def serverGet(self):
        response = requests.get('http://smart-farm.xyz/')
        data = response.json()
        return data
    

    
    def __exit__(self):
        GPIO.cleanup()
        print("GPIO cleaned up")
        return True



#### Options ####

# Define Pi Pins
pins = {
    'moisture' : 17,
    'light' : 27,
}

streamTime = 10 # Time to print out data (seconds)
deplayTime = 1 # Delay between prints


#### Init ####

bench = TestBench(pins) # Init Bench Class


#### Main #### 

# Print Data Steam
startTime = time.time()
while time.time() - startTime < streamTime:
    betterPrint(f"Moisture: {bench.getMoisture()}", "cyan")
    time.sleep(deplayTime)