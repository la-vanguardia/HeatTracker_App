import serial
import time
import json

DatosCOM = serial.Serial("COM3",19200)
time.sleep(1)


for i in [0, 1, 2, 3]:
    DatosIN= DatosCOM.readline().decode('utf-8')
    DatosJson = json.loads(DatosIN)
    Posicion = DatosJson['Pos']
    Temperatura = DatosJson['Temp']


