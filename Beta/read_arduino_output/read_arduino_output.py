import serial
#import time

def is_wrist_bad():
    #arduino = serial.Serial("com6", 9600) # Gabe's computer
    arduino = serial.Serial("/dev/ttyACM0", 9600) # For Joel's computer
    #print("Established Serial Connection to Arduino")
    arduino_data = arduino.readline()
    #print(arduino_data)
    #decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    #decoded_values = arduino_data.decode().strip()
    # list_values = decoded_values.split(" | ")
    #print(decoded_values)
    return arduino_data == b"1\r\n"
