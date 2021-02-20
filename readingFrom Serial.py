import serial


arduino = serial.Serial('com3', 9600)
print('Established serial connection to Arduino')
while True:
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data.decode("utf-8"))
    print(decoded_values)
