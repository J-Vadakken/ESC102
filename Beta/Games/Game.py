import pygame
from pygame.locals import *
import os
import serial
#import time

# # Uncomment for when arudion is running
# Basically, we want is_wrist_bad to output True when the wrist is bad
# and False when the wrist is good

# arduino_ = serial.Serial("/dev/ttyACM0", 9600) # For Joel's computer

# def is_wrist_bad(arduino):
#     #arduino = serial.Serial("com6", 9600) # Gabe's computer
#     #arduino = serial.Serial("/dev/ttyACM0", 9600) # For Joel's computer
#     #print("Established Serial Connection to Arduino")
#     arduino_data = arduino.readline()
#     #print(arduino_data)
#     #decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
#     #decoded_values = arduino_data.decode().strip()
#     # list_values = decoded_values.split(" | ")
#     #print(decoded_values)
#     return arduino_data == b"1\r\n"


# Testing Comment this out when we want the actual rasbarry pi running
arduino_ = None
i_ = 0
def is_wrist_bad(arduino):
    return True
# To here


def draw_wrist(screen):
    global i_
    if is_wrist_bad(arduino_) and i_ >= 40:
        screen.blit(warn_img, (SCREEN_WIDTH/2 - 250, 40))
    i_ += 1
    if i_ >= 80:
        i_ = 0



pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
img_path = os.path.join(os.path.dirname(__file__), "Warning.png")
pygame.display.set_caption('Piano Assitant')
warn_img = pygame.image.load(img_path)
clock = pygame.time.Clock()
bg_color = (255, 255, 255)
outline_color = (0, 0, 0)
run = True
raise_wrist = pygame.Rect((300, 250, 50, 50))

class piano_tile:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def draw(self, screen):
        self.rect.y += 1
        if (self.rect.y > SCREEN_HEIGHT):
            self.rect.y = 0 - self.rect.height
        pygame.draw.rect(screen, self.color, self.rect)

piano_tile_height = 200
piano_tile1 = piano_tile(0               , 0                  , SCREEN_WIDTH/5, piano_tile_height, (0,0,0))
piano_tile2 = piano_tile(SCREEN_WIDTH/5  , piano_tile_height*2, SCREEN_WIDTH/5, piano_tile_height, (0,0,0))
piano_tile3 = piano_tile(SCREEN_WIDTH/5*2, piano_tile_height  , SCREEN_WIDTH/5, piano_tile_height, (0,0,0))
piano_tile4 = piano_tile(SCREEN_WIDTH/5*3, piano_tile_height*4, SCREEN_WIDTH/5, piano_tile_height, (0,0,0))
piano_tile5 = piano_tile(SCREEN_WIDTH/5*4, piano_tile_height*5, SCREEN_WIDTH/5, piano_tile_height, (0,0,0))
piano_tiles = [piano_tile1, piano_tile2, piano_tile3, piano_tile4, piano_tile5]

while run:
    clock.tick(60)
    
    pygame.draw.rect(screen, bg_color, (0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    for i in range(5):
        for piano_tile in piano_tiles:
            piano_tile.draw(screen)
    for i in range(5):
        w = 0+SCREEN_WIDTH/5*i
        pygame.draw.rect(screen, outline_color, (w, 0, SCREEN_WIDTH/5, SCREEN_HEIGHT), 1)


    draw_wrist(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()