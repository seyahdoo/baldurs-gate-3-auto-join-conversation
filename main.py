# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Initial Release Date: 05/08/2023

import pyautogui
import time
import msvcrt as m
import os

PNG_PATH = "listen-in.png"
VERSION = "1.0.1"

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
Version: v1.0.1
        """)
    return

def do_loop():
    print("Trying to locate the listen in button")
    while True:
        try:
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen(PNG_PATH)
            print(f"Clicking on listen in button on ({x}, {y})")
            pyautogui.click(x, y)
        except FileNotFoundError as e: error_out(e)
        except TypeError as e: pass
        except Exception as e: error_out(e)

def error_out(e):
    print(e)
    print("Press any key to exit...", end="", flush=True)
    m.getch()
    exit(0)

if __name__ == "__main__":
    main()