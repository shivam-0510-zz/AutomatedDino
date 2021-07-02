import pyautogui
from PIL import Image, ImageGrab
import time

while True:
    image = ImageGrab.grab().convert('L') # translating to greyscale (faster)
    data = image.load()

    # cactus
    for i in range (250, 300):
        for j in range(550, 600):
            data[i, j] = 0
    
    # bird
    for i in range (200, 250):
        for j in range(400, 550):
            data[i, j] =150
    
    image.show()
    break