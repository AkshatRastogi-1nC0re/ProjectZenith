import pyautogui
import time

def spam(text):
    while True:
        # time.sleep(1)I CAN DO THIS ALL DAY
        pyautogui.typewrite(text)
        pyautogui.press('enter')