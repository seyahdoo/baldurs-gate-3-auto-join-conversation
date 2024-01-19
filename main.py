# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Initial Release Date: 05/08/2023

import pyautogui
import time
import msvcrt as m
import os
import sys
from version import version
import keyboard
from pynput.keyboard import Key, Listener

PNG_PATH = "listen-in.png"

def main():
    print_intro()    
    do_loop()

def print_intro():
    print(f"""
######################################################
######################################################
####                                              ####
####    Baldurs Gate 3 Auto Join Conversations    ####
####                                              ####
######################################################
######################################################

Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
Release Date: 05/08/2023
Version: v{version}
        """)
    return

def do_loop():
    print("Trying to locate the listen in button")
    while(True):
        if keyboard.is_pressed('1'):
            shananigan((242, 1340))
        if keyboard.is_pressed('2'):
            shananigan((455, 1171))
        if keyboard.is_pressed('esc'):
            return
        time.sleep(0.1)

def shananigan(pos):
    cur = pyautogui.position()
    pyautogui.click(pos)
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.3)
    wait_till("cancel.png")
    print("wait done")
    time.sleep(0.5)
    print("clicking back")
    pyautogui.click(cur)
    
    # for i in range(0, 50):
    #     # click_to("bubble.png")
    #     pyautogui.click((1914, 544))
    #     # return
    #     for i in range(0, i+1):
    #         pyautogui.press("down")
    #     pyautogui.click((455, 1171))
    #     pyautogui.press("enter")
    #     wait_till("cancel.png")
    #     time.sleep(1)
    #     if keyboard.is_pressed('esc'):
    #         return

def wait_till(path):
    print(path)
    while(True):
        if pyautogui.locateCenterOnScreen(path, confidence=0.95) is None:
            return
        time.sleep(0.3)

# def click_to(path):
#     time.sleep(0.3)
#     print(path)
#     x, y = pyautogui.locateCenterOnScreen(path, confidence=0.95)
#     print(f"Clicking on ({x}, {y})")
#     pyautogui.click(x, y)
#     return

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)

# def error_out(e):
#     print(e)
#     print("Press any key to exit...", end="", flush=True)
#     m.getch()
#     exit(0)

if __name__ == "__main__":
    main()