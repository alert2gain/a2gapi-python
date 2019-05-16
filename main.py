import requests
import json
import datetime
import time
import random

from collections import namedtuple

# Demo object named sensor, with 4 attributes related to weather stations
class Sensor:
    def __init__(self, name, temperature, humidity, lastread):
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.lastread = lastread


# Method to send data to A2G InpuStream API
def sendData(station):
    stationData = { "Station": station.name, "data": {"temperature": station.temperature, "humidity": station.humidity, "updated": station.lastread}}
    jsonData = json.dumps(stationData)

    url = 'https://listen.a2g.io/v1/testing/inputstream'
    data = {"IKEY": "[YOUR_INPUTSTREAM_KEY]", "Data": jsonData }
    headers = {'x-api-key': '[YOUR_API_KEY]'}
    response = requests.post(url, json=data, headers=headers)

    responseObject = json.loads(response.content, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    if responseObject.Status == "OK":
        print("Success!")
        return True
    else:
        print("Oops, an error ocurred: ", responseObject.Message)
        return False


def run_sensors():
    #Initialize the sensor with your logic
    sensor = Sensor("Station 1", 10, 15, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    sensorList = [sensor]
    while True:
        # We iterate over our sensor list
        for sensor in sensorList:
            # We update the sensor readings (random in this example)
            sensor.temperature = random.uniform(10, 35)
            sensor.humidity = random.uniform(0, 100)
            sensor.lastread = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

            status = sendData(sensor)

            # We can retry or log if the method was unable to send the data successfully

            time.sleep(30)

if __name__ == '__main__':
    run_sensors()