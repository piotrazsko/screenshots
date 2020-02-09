#!/usr/local/bin/python
# coding=utf-8
import numpy as np
import pyautogui
import imutils
import cv2
# from pynput.mouse import Listener
from pynput.keyboard import Key, Listener

index = 0

def inc():
	global index
	index +=1
	print(index)

def on_press(key):

    print('{0} pressed'.format(key))
    if 	key == Key.esc:
        return False
    if key == Key.enter:
        image = pyautogui.screenshot(region=(0,0, 1400, 1000))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        inc()
        cv2.imwrite( str(index)+ '.png' , image)
		# return 
	

def on_click(x, y, button, pressed):
        print("Mouse clicked")

with Listener( on_press=on_press,on_click=on_click) as listener:
    listener.join()

    
