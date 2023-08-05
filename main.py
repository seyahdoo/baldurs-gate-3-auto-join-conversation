# Author: Seyyid Ahmed Doğan (seyahdoo, seyahdoo@gmail.com)
# Initial Release Date: 05/08/2023

import pyautogui
import time

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
    print("trying to locate the listen in button")
    while True:
        try:
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen(PNG_PATH)
            print(f"clicking on listen in button on ({x}, {y})")
            pyautogui.click(x, y)
        except FileNotFoundError as e: print(e); exit(1)
        except TypeError as e: pass
        except Exception as e: print(e); exit(1)

if __name__ == "__main__":
    main()