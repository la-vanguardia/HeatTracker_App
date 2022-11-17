import serial
import time
import json

port = serial.Serial("COM3", 19200)
time.sleep(1)

for i in [0, 1, 2, 3]:
    data = port.readline().decode('utf-8')
    jsonData = json.loads(data)
    position = jsonData['Pos']
    temp = jsonData['Temp']


