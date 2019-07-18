from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
import time

class Cordinates():
    replayBtn = (292,426)
    dino = (168,431)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (203,431,221,454)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())

def main():
    restartGame()
    while True:
        if (imageGrab() != 661):
            pressSpace()
            time.sleep(0.1)

main()