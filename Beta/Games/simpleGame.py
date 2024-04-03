import pygame

import serial
#import time

arduino = serial.Serial("/dev/ttyACM0", 9600) # For Joel's computer

def is_wrist_bad(arduino):
    #arduino = serial.Serial("com6", 9600) # Gabe's computer
    #arduino = serial.Serial("/dev/ttyACM0", 9600) # For Joel's computer
    #print("Established Serial Connection to Arduino")
    arduino_data = arduino.readline()
    #print(arduino_data)
    #decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    #decoded_values = arduino_data.decode().strip()
    # list_values = decoded_values.split(" | ")
    #print(decoded_values)
    return arduino_data == b"1\r\n"

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True

raise_wrist = pygame.Rect((300, 250, 50, 50))

while run:
    if is_wrist_bad(arduino):
        pygame.draw.rect(screen, (255,0,0), raise_wrist)
    else:
        pygame.draw.rect(screen, (0,0,0), raise_wrist)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()