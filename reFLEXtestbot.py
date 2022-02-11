from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#RGB(255,0,0)
#each round is 15 seconds
#targets start spawning 3 seconds apart
#rounds get 0.2 seconds faster each time
#there are about 17 rounds

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.01)


time.sleep(6)
while keyboard.is_pressed('q') == False:
    time_start = time.time()
    pic = pyautogui.screenshot(region=(191,167,957,540))
    
    width, height = pic.size
             
    for x in range(0,width,5):
        for y in range(0,height,5):

            r,g,b = pic.getpixel((x,y))
            
            if r == 0 and g == 0 and b == 0:
                click(x+191,y+177)
                break
