# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Initial Release Date: 05/08/2023
# Version: 1.0

import pyautogui
import time
import os

version = "1.0"

print(f"Baldurs Gate 3 Auto Join Conversations v{version}")
print(f"Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)")
print(f"Initial Release Date: 05/08/2023")

png_path = "listen-in.png"

while True:
    try:
        time.sleep(1)
        location = pyautogui.locateOnScreen(png_path)
        if(location == None):
            continue
        print(f"found listen in button {location}")
        x = location.left + location.width/2
        y = location.top + location.height/2
        print(f"clicking listen in button on ({x}, {y})")
        pyautogui.click(x, y)
    except Exception as e:
        print(e)


