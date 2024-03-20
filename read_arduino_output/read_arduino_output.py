import serial
import time

def main_fcn():
    arduino = serial.Serial("com6", 9600)
    print("Established Serial Connection to Arduino")
    while True:
        arduino_data = arduino.readline()
        decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
        list_values = decoded_values.split(" | ")

        print(f"Collected readings from Arduino: {list_values}")

        arduino_data = 0
        list_values.clear()

        print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

'''_________________________________________________________________'''

list_values = []
list_in_floats = []

print("Program Started")

main_fcn()