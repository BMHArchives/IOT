import serial
s = serial.Serial("COM#",9600)
while True:
      print(s.readline())