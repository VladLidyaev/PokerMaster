from PIL import Image
import pyautogui
import time

time.sleep(4)

image = pyautogui.screenshot('sss.png')

print(str(pyautogui.pixel(1170,731)))