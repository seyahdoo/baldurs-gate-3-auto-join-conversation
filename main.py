# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Initial Release Date: 05/08/2023

import pyautogui
import time
import msvcrt as m
import os
import sys
from version import version

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
    while True:
        try:
            time.sleep(1)
            path = resource_path(PNG_PATH)
            x, y = pyautogui.locateCenterOnScreen(path, confidence=0.70)
            print(f"Clicking on listen in button on ({x}, {y})")
            pyautogui.click(x, y)
        except FileNotFoundError as e: error_out(e)
        except TypeError as e: pass
        except Exception as e: error_out(e)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def error_out(e):
    print(e)
    print("Press any key to exit...", end="", flush=True)
    m.getch()
    exit(0)

if __name__ == "__main__":
    main()