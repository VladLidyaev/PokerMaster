import pyautogui
import time
import os

time.sleep(2)

pixel_hand_1_X = 572  # Пиксели для обнаружения карт на столе и в руке
pixel_hand_1_Y = 500

pixel_hand_2_X = 644
pixel_hand_2_Y = 500

card_w = 18
card_h = 25

i = 1
while True:
    if str(pyautogui.pixel(577,500)) == 'RGB(red=255, green=255, blue=255)':
        image = pyautogui.screenshot('Hunter.png')
        im_hand_1 = image.crop((pixel_hand_1_X, pixel_hand_1_Y, (pixel_hand_1_X + card_w), (pixel_hand_1_Y + card_h))).save(str(i))
        i += 1
        im_hand_2 = image.crop((pixel_hand_2_X, pixel_hand_2_Y, (pixel_hand_2_X + card_w), (pixel_hand_2_Y + card_h))).save()
        stop = False
        while stop == False:
            if str(pyautogui.pixel(577,500)) != 'RGB(red=255, green=255, blue=255)':
                stop = True
    os.remove("/Users/vlad/PycharmProjects/PokerMaster/venv/Hunter.png")