import sys
sys.path.insert(1, './read_arduino_output/')
import read_arduino_output
from read_arduino_output import is_wrist_bad
# instructions for use: Make sure you are cd'd into the Beta folder when you run this file

while True:
    print(is_wrist_bad())
    