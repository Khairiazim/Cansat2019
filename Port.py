import serial
# windows 7
ser = serial.Serial('COM3', baudrate = 9600)

while 1:
     data = ser.readline()
     print(data)

