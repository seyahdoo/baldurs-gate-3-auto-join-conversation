# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Initial Release Date: 05/08/2023

import pyautogui
import time
import msvcrt as m
import os
import sys
import json
import keyboard
from screeninfo import get_monitors
from version import version

# Global variable to control the pause state
paused = False

def main():
    try:
        print_intro()
        png_path, confidence, pause_hotkey = load_settings()
        keyboard.add_hotkey(pause_hotkey, lambda : toggle_pause(pause_hotkey))
        do_loop(png_path, confidence)
    except Exception as e: error_out(e)
    return

def toggle_pause(pause_hotkey):
    global paused
    paused = not paused
    if paused:
        print(f"Script is paused. Press {pause_hotkey} again to resume.")
    else:
        print(f"Script is resumed. Press {pause_hotkey} again to pause.")

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

def load_settings():
    print("loading settings from settings.json")
    with open("settings.json", "r") as f:
        settings = json.load(f)
        confidence = float(settings["confidence"])
        print(f"setting confidence to {confidence}")
        resolution_height = settings["resolution_height"]
        if resolution_height == "auto-detect":
            print("auto detecting screen height")
            for m in get_monitors():
                if m.is_primary:
                    resolution_height = m.height
                    print(f"detected screen height {resolution_height}")
        png_path = f"listen-in-{resolution_height}.png"
        print(f"using png path {png_path}")
        pause_hotkey = settings["pause_hotkey"]
    return png_path, confidence, pause_hotkey

def do_loop(png_path, confidence):
    print("-------------------------------------")
    print("Trying to locate the listen in button")
    while True:
        if not paused:
            try:
                time.sleep(1)
                x, y = pyautogui.locateCenterOnScreen(png_path, confidence=confidence)
                print(f"Clicking on listen in button on ({x}, {y})")
                pyautogui.click(x, y)
            except TypeError as e: pass
        else:
            time.sleep(0.5)
    return

def error_out(e):
    print(e)
    print("Press any key to exit...", end="", flush=True)
    m.getch()
    exit(0)
    return

if __name__ == "__main__":
    main()
