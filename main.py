# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Written on: 05/08/2023


import pyautogui
import time

while True:
    try:
        time.sleep(1)
        location = pyautogui.locateOnScreen('listen-in.png')
        if(location == None):
            continue
        print(f"found listen in button {location}")
        x = location.left + location.width/2
        y = location.top + location.height/2
        print(f"clicking listen in button on ({x}, {y})")
        pyautogui.click(x, y)
    except Exception as e:
        print(e)

