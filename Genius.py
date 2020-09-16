import os
import time

import PIL.ImageOps
import pyautogui
import pytesseract
from PIL import Image

time.sleep(1)

# БЛОК КОНСТАНТ

Small_Blind = 50
Big_Blind = 100

if True:
    WHITE_COLOR = 'RGB(red=255, green=255, blue=255)'

    TESERACT_COLOR_RED = 7  # Кодировка цвета для определения границ поля ставок игроков
    TESERACT_COLOR_GREEN = 76
    TESERACT_COLOR_BLUE = 23

    Start_Testing_Pixel_X = 577  # Пиксель для определения наличия карт на руках
    Start_Testing_Pixel_Y = 500

    Fold_Button_Pixel_X = 715
    Fold_Button_Pixel_Y = 757

    Stop_Pixel_X = 50  # Пиксель для остановки программы по вычислению решения и дальнейший выход со стола
    Stop_Pixel_Y = 50
    Color_for_stop = 'RGB(red=219, green=219, blue=220)'

    Activator_Pixel_X = 900  # Пиксель для определения количества кнопок
    Activator_Pixel_Y = 700

    Turn_Pixel_X = 1170  # Пиксель для определения моей очереди хода
    Turn_Pixel_Y = 731

    Three_Cards_Pixel_X = 579  # Пиксель опредляющий 3 первые карты на столе
    Three_Cards_Pixel_Y = 267

    Four_Cards_Pixel_X = 730  # Пиксель опредляющий 4 карты на столе
    Four_Cards_Pixel_Y = 267

    Five_Cards_Pixel_X = 809  # Пиксель опредляющий 5 карт на столе
    Five_Cards_Pixel_Y = 267

    card_w = 18
    card_h = 40

    pixel_hand_1_X = 572  # Пиксели для обнаружения карт на столе и в руке
    pixel_hand_1_Y = 500

    pixel_hand_2_X = 644
    pixel_hand_2_Y = 500

    pixel_table_1_X = 455
    pixel_table_1_Y = 265

    pixel_table_2_X = 532
    pixel_table_2_Y = 265

    pixel_table_3_X = 608
    pixel_table_3_Y = 265

    pixel_table_4_X = 684
    pixel_table_4_Y = 265

    pixel_table_5_X = 761
    pixel_table_5_Y = 265

    My_Bank_Pixel_X = 560
    My_Bank_Pixel_Y = 590

    Bank_w = 110
    Bank_h = 25

    My_label_pixel_X = 543
    My_label_pixel_Y = 495

    Left_Button_Pixel_X = 670
    Left_Button_Pixel_Y = 740

    Center_Button_Pixel_X = 880
    Center_Button_Pixel_Y = 740

    Right_Button_Pixel_X = 1090
    Right_Button_Pixel_Y = 740

    Button_w = 160
    Button_h = 40

    Player_1_Testing_Pixel_X = 218
    Player_1_Testing_Pixel_Y = 523
    Color_Of_Absence_Player_1 = '(26, 28, 38, 255)'
    Player_1_Activity_Pixel_X = 234  # Пикслеь для определения участия игрока
    Player_1_Activity_Pixel_Y = 461
    Player_1_Presence_Of_Label_Pixel_X = 362  # Пиксель для определния наличия фишки МБ/ББ
    Player_1_Presence_Of_Label_Pixel_Y = 400
    Player_1_Bet_Pixel_X = 412  # Пиксель для Teseract, для определения ставки игрока
    Player_1_Bet_Pixel_Y = 419
    Player_1_Bank_Pixel_X = 220
    Player_1_Bank_Pixel_Y = 512

    Player_2_Testing_Pixel_X = 110
    Player_2_Testing_Pixel_Y = 359
    Color_Of_Absence_Player_2 = '(38, 40, 52, 255)'
    Player_2_Activity_Pixel_X = 120
    Player_2_Activity_Pixel_Y = 302
    Player_2_Presence_Of_Label_Pixel_X = 291
    Player_2_Presence_Of_Label_Pixel_Y = 287
    Player_2_Bet_Pixel_X = 339
    Player_2_Bet_Pixel_Y = 362
    Player_2_Bank_Pixel_X = 110
    Player_2_Bank_Pixel_Y = 347

    Player_3_Testing_Pixel_X = 159
    Player_3_Testing_Pixel_Y = 200
    Color_Of_Absence_Player_3 = '(44, 44, 56, 255)'
    Player_3_Activity_Pixel_X = 168
    Player_3_Activity_Pixel_Y = 144
    Player_3_Presence_Of_Label_Pixel_X = 420
    Player_3_Presence_Of_Label_Pixel_Y = 215
    Player_3_Bet_Pixel_X = 367
    Player_3_Bet_Pixel_Y = 237
    Player_3_Bank_Pixel_X = 151
    Player_3_Bank_Pixel_Y = 189

    Player_4_Testing_Pixel_X = 372
    Player_4_Testing_Pixel_Y = 119
    Color_Of_Absence_Player_4 = '(46, 48, 61, 255)'
    Player_4_Activity_Pixel_X = 381
    Player_4_Activity_Pixel_Y = 63
    Player_4_Presence_Of_Label_Pixel_X = 603
    Player_4_Presence_Of_Label_Pixel_Y = 163
    Player_4_Bet_Pixel_X = 515
    Player_4_Bet_Pixel_Y = 187
    Player_4_Bank_Pixel_X = 365
    Player_4_Bank_Pixel_Y = 113

    Player_5_Testing_Pixel_X = 906
    Player_5_Testing_Pixel_Y = 124
    Color_Of_Absence_Player_5 = '(47, 47, 49, 255)'
    Player_5_Activity_Pixel_X = 761
    Player_5_Activity_Pixel_Y = 60
    Player_5_Presence_Of_Label_Pixel_X = 830
    Player_5_Presence_Of_Label_Pixel_Y = 184
    Player_5_Bet_Pixel_X = 777
    Player_5_Bet_Pixel_Y = 165
    Player_5_Bank_Pixel_X = 794
    Player_5_Bank_Pixel_Y = 114

    Player_6_Testing_Pixel_X = 1119
    Player_6_Testing_Pixel_Y = 201
    Color_Of_Absence_Player_6 = '(44, 44, 46, 255)'
    Player_6_Activity_Pixel_X = 974
    Player_6_Activity_Pixel_Y = 138
    Player_6_Presence_Of_Label_Pixel_X = 949
    Player_6_Presence_Of_Label_Pixel_Y = 244
    Player_6_Bet_Pixel_X = 898
    Player_6_Bet_Pixel_Y = 212
    Player_6_Bank_Pixel_X = 1006
    Player_6_Bank_Pixel_Y = 189

    Player_7_Testing_Pixel_X = 1196
    Player_7_Testing_Pixel_Y = 338
    Color_Of_Absence_Player_7 = '(38, 38, 40, 255)'
    Player_7_Activity_Pixel = pyautogui.pixel(1022, 296)
    Player_7_Activity_Pixel_X = 1022
    Player_7_Activity_Pixel_Y = 296
    Player_7_Presence_Of_Label_Pixel_X = 986
    Player_7_Presence_Of_Label_Pixel_Y = 396
    Player_7_Bet_Pixel_X = 939
    Player_7_Bet_Pixel_Y = 362
    Player_7_Bank_Pixel_X = 1054
    Player_7_Bank_Pixel_Y = 347

    Player_8_Testing_Pixel_X = 1063
    Player_8_Testing_Pixel_Y = 526
    Color_Of_Absence_Player_8 = '(27, 26, 30, 255)'
    Player_8_Activity_Pixel_X = 908
    Player_8_Activity_Pixel_Y = 457
    Player_8_Presence_Of_Label_Pixel_X = 852
    Player_8_Presence_Of_Label_Pixel_Y = 455
    Player_8_Bet_Pixel_X = 843
    Player_8_Bet_Pixel_Y = 419
    Player_8_Bank_Pixel_X = 945
    Player_8_Bank_Pixel_Y = 512


# БЛОК КЛАССОВ

class Player:
    def __init__(self, name, bank, on_or_off, active, actual_bet, sum_bet, role):
        self.name = name
        self.bank = bank
        self.onoff = on_or_off
        self.active = active
        self.actual_bet = actual_bet
        self.sum_bet = sum_bet
        self.role = role

    def name(self):
        return str(self.name())

    def bank(self):
        return int(self.bank())

    def on_or_off(self):
        return str(self.onoff)

    def active(self):
        return str(self.active())

    def actual_bet(self):
        return int(self.actual_bet())

    def sum_bet(self):
        return int(self.sum_bet())

    def role(self):
        return str(self.role())

    def new_bank(self, new_bank):
        self.bank = new_bank

    def new_role(self, new_role):
        self.role = new_role

    def new_active(self, new_active):
        self.active = new_active

    def new_on_or_off(self, new_onoffer):
        self.on_or_off = new_onoffer

    def new_actual_bet(self, new_bet):
        self.actual_bet = new_bet

    def nem_sum_bet(self, new_sum_bet):
        self.sum_bet = new_sum_bet


class Card:
    def __init__(self, name, value, suit):
        self.name = name
        self.value = value
        self.suit = suit

    def name(self):
        return self.name()

    def value(self):
        return self.value()

    def suit(self):
        return self.suit()


# БЛОК ФУНКЦИЙ

def waiting_start():  # Ожидание пока карты придут в руку

    def start_playing():  # Определяет наличие карт на руках
        if str(pyautogui.pixel(Start_Testing_Pixel_X, Start_Testing_Pixel_Y)) == WHITE_COLOR:
            return True
        else:
            return False

    i = 0
    while i == 0:
        if start_playing() == True:
            i = 1


def waiting_my_turn():  # Функция ожидания своего хода
    chek_color = 'RGB(red=174, green=29, blue=19)'

    def my_move():  # Функция сравнения пикселей для ожидания своего хода
        if str(pyautogui.pixel(Turn_Pixel_X, Turn_Pixel_Y)) == chek_color:
            return True
        else:
            return False

    i = 0
    while i == 0:
        if my_move() == True:
            i = 1


def stop_playing():  # Программа прекращает работу при открытии вкладки СТОЛ
    if str(pyautogui.pixel(Stop_Pixel_X, Stop_Pixel_Y)) == Color_for_stop:
        return True
    else:
        return False


def now_stage(image_input):  # Определение количесвта карт на столе
    image = image_input
    white_color_for_getpixel = '(255, 255, 255, 255)'

    if str(image.getpixel((Three_Cards_Pixel_X, Three_Cards_Pixel_Y))) == white_color_for_getpixel:
        if str(image.getpixel((Four_Cards_Pixel_X, Four_Cards_Pixel_Y))) == white_color_for_getpixel:
            if str(image.getpixel((Five_Cards_Pixel_X, Five_Cards_Pixel_Y))) == white_color_for_getpixel:
                return 4
            else:
                return 3
        else:
            return 2
    else:
        return 1


def check_hands_cards(image_input):  # Определяет какие карты в руке
    image = image_input

    im_hand_1 = image.crop((pixel_hand_1_X, pixel_hand_1_Y, (pixel_hand_1_X + card_w), (pixel_hand_1_Y + card_h)))
    im_hand_2 = image.crop((pixel_hand_2_X, pixel_hand_2_Y, (pixel_hand_2_X + card_w), (pixel_hand_2_Y + card_h)))

    hand_1 = ','
    hand_2 = ','

    for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
        if i == 11:
            i = 'J'
        if i == 12:
            i = 'Q'
        if i == 13:
            i = 'K'
        if i == 14:
            i = 'A'

        for j in [1, 2, 3, 4]:
            if j == 1:
                j = 'bu'
            if j == 2:
                j = 'ch'
            if j == 3:
                j = 'kr'
            if j == 4:
                j = 'pi'

            name = str(i) + '_' + str(j) + '_hand'
            test_im = Image.open('/Users/vlad/PycharmProjects/PokerMaster/Cards/Hand/' + str(name) + '.png')

            if im_hand_1.histogram() == test_im.histogram():
                hand_1 = str(i) + ',' + j

            if im_hand_2.histogram() == test_im.histogram():
                hand_2 = str(i) + ',' + j

    if hand_1 == ',':
        hand_1 = '0'
    if hand_2 == ',':
        hand_2 = '0'

    return (hand_1 + ';' + hand_2)


def check_table_cards(image_input):
    image = image_input

    im_table_1 = image.crop((pixel_table_1_X, pixel_table_1_Y, (pixel_table_1_X + card_w), (pixel_table_1_Y + card_h)))
    im_table_2 = image.crop((pixel_table_2_X, pixel_table_2_Y, (pixel_table_2_X + card_w), (pixel_table_2_Y + card_h)))
    im_table_3 = image.crop((pixel_table_3_X, pixel_table_3_Y, (pixel_table_3_X + card_w), (pixel_table_3_Y + card_h)))
    im_table_4 = image.crop((pixel_table_4_X, pixel_table_4_Y, (pixel_table_4_X + card_w), (pixel_table_4_Y + card_h)))
    im_table_5 = image.crop((pixel_table_5_X, pixel_table_5_Y, (pixel_table_5_X + card_w), (pixel_table_5_Y + card_h)))

    table_1 = ','
    table_2 = ','
    table_3 = ','
    table_4 = ','
    table_5 = ','

    for i in [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
        if i == 11:
            i = 'J'
        if i == 12:
            i = 'Q'
        if i == 13:
            i = 'K'
        if i == 14:
            i = 'A'

        for j in [1, 2, 3, 4]:
            if j == 1:
                j = 'bu'
            if j == 2:
                j = 'ch'
            if j == 3:
                j = 'kr'
            if j == 4:
                j = 'pi'

            name = str(i) + '_' + str(j) + '_table'
            test_im = Image.open('/Users/vlad/PycharmProjects/PokerMaster/Cards/Table/' + str(name) + '.png')

            if im_table_1.histogram() == test_im.histogram():
                table_1 = str(i) + ',' + j
            if im_table_2.histogram() == test_im.histogram():
                table_2 = str(i) + ',' + j
            if im_table_3.histogram() == test_im.histogram():
                table_3 = str(i) + ',' + j
            if im_table_4.histogram() == test_im.histogram():
                table_4 = str(i) + ',' + j
            if im_table_5.histogram() == test_im.histogram():
                table_5 = str(i) + ',' + j
    if table_1 == ',':
        table_1 = '0'
    if table_2 == ',':
        table_2 = '0'
    if table_3 == ',':
        table_3 = '0'
    if table_4 == ',':
        table_4 = '0'
    if table_5 == ',':
        table_5 = '0'

    return (table_1 + ';' + table_2 + ';' + table_3 + ';' + table_4 + ';' + table_5)


def who_is_playing(image_input):
    image = image_input
    PLAYERS = []

    if str(image.getpixel((Player_1_Testing_Pixel_X, Player_1_Testing_Pixel_Y))) != Color_Of_Absence_Player_1:
        PLAYERS.append(1)
    if str(image.getpixel((Player_2_Testing_Pixel_X, Player_2_Testing_Pixel_Y))) != Color_Of_Absence_Player_2:
        PLAYERS.append(2)
    if str(image.getpixel((Player_3_Testing_Pixel_X, Player_3_Testing_Pixel_Y))) != Color_Of_Absence_Player_3:
        PLAYERS.append(3)
    if str(image.getpixel((Player_4_Testing_Pixel_X, Player_4_Testing_Pixel_Y))) != Color_Of_Absence_Player_4:
        PLAYERS.append(4)
    if str(image.getpixel((Player_5_Testing_Pixel_X, Player_5_Testing_Pixel_Y))) != Color_Of_Absence_Player_5:
        PLAYERS.append(5)
    if str(image.getpixel((Player_6_Testing_Pixel_X, Player_6_Testing_Pixel_Y))) != Color_Of_Absence_Player_6:
        PLAYERS.append(6)
    if str(image.getpixel((Player_7_Testing_Pixel_X, Player_7_Testing_Pixel_Y))) != Color_Of_Absence_Player_7:
        PLAYERS.append(7)
    if str(image.getpixel((Player_8_Testing_Pixel_X, Player_8_Testing_Pixel_Y))) != Color_Of_Absence_Player_8:
        PLAYERS.append(8)

    return (str(PLAYERS).partition('[')[2].rpartition(']')[0])


def who_is_active(image_input):
    image = image_input
    PLAYERS = []
    white_color_for_getpixel = '(255, 255, 255, 255)'

    if str(image.getpixel((Player_1_Activity_Pixel_X, Player_1_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(1)
    if str(image.getpixel((Player_2_Activity_Pixel_X, Player_2_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(2)
    if str(image.getpixel((Player_3_Activity_Pixel_X, Player_3_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(3)
    if str(image.getpixel((Player_4_Activity_Pixel_X, Player_4_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(4)
    if str(image.getpixel((Player_5_Activity_Pixel_X, Player_5_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(5)
    if str(image.getpixel((Player_6_Activity_Pixel_X, Player_6_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(6)
    if str(image.getpixel((Player_7_Activity_Pixel_X, Player_7_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(7)
    if str(image.getpixel((Player_8_Activity_Pixel_X, Player_8_Activity_Pixel_Y))) == white_color_for_getpixel:
        PLAYERS.append(8)

    return (str(PLAYERS).partition('[')[2].rpartition(']')[0])


def who_is_starting(image_input, players_list):  # Опредление выборки среди игроков - 3 первых игрока после диллера
    image = image_input
    PLAYERS = []

    if int(str(image.getpixel((My_label_pixel_X, My_label_pixel_Y))).rpartition(',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(0)

    if int(str(image.getpixel((Player_1_Presence_Of_Label_Pixel_X, Player_1_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(1)

    if int(str(image.getpixel((Player_2_Presence_Of_Label_Pixel_X, Player_2_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(2)

    if int(str(image.getpixel((Player_3_Presence_Of_Label_Pixel_X, Player_3_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(3)

    if int(str(image.getpixel((Player_4_Presence_Of_Label_Pixel_X, Player_4_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(4)

    if int(str(image.getpixel((Player_5_Presence_Of_Label_Pixel_X, Player_5_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(5)

    if int(str(image.getpixel((Player_6_Presence_Of_Label_Pixel_X, Player_6_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(6)

    if int(str(image.getpixel((Player_7_Presence_Of_Label_Pixel_X, Player_7_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(7)

    if int(str(image.getpixel((Player_8_Presence_Of_Label_Pixel_X, Player_8_Presence_Of_Label_Pixel_Y))).rpartition(
            ',')[0].rpartition(' ')[2]) >= 200:
        PLAYERS.append(8)

    if str(PLAYERS) != '':
        diller = int(str(PLAYERS).partition('[')[2].rpartition(']')[0])
    else:
        diller = 5
    ROLES = []

    for i in [1, 2, 3]:
        number = ((diller + 1) % 9)
        if ('Player_' + str(number)) in players_list:
            ROLES.append(number)
            diller = number
        else:
            while (('Player_' + str(number)) in players_list) == False:
                number = (number + 1) % 9
            ROLES.append(number)
            diller = number

    return str(ROLES).partition('[')[2].rpartition(']')[0]


def check_players_banks(image_input, players_list):
    Bank_list = []
    image = image_input

    im_bank_1 = image.crop((Player_1_Bank_Pixel_X, Player_1_Bank_Pixel_Y, (Player_1_Bank_Pixel_X + Bank_w),
                            (Player_1_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_2 = image.crop((Player_2_Bank_Pixel_X, Player_2_Bank_Pixel_Y, (Player_2_Bank_Pixel_X + Bank_w),
                            (Player_2_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_3 = image.crop((Player_3_Bank_Pixel_X, Player_3_Bank_Pixel_Y, (Player_3_Bank_Pixel_X + Bank_w),
                            (Player_3_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_4 = image.crop((Player_4_Bank_Pixel_X, Player_4_Bank_Pixel_Y, (Player_4_Bank_Pixel_X + Bank_w),
                            (Player_4_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_5 = image.crop((Player_5_Bank_Pixel_X, Player_5_Bank_Pixel_Y, (Player_5_Bank_Pixel_X + Bank_w),
                            (Player_5_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_6 = image.crop((Player_6_Bank_Pixel_X, Player_6_Bank_Pixel_Y, (Player_6_Bank_Pixel_X + Bank_w),
                            (Player_6_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_7 = image.crop((Player_7_Bank_Pixel_X, Player_7_Bank_Pixel_Y, (Player_7_Bank_Pixel_X + Bank_w),
                            (Player_7_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_8 = image.crop((Player_8_Bank_Pixel_X, Player_8_Bank_Pixel_Y, (Player_8_Bank_Pixel_X + Bank_w),
                            (Player_8_Bank_Pixel_Y + Bank_h))).convert('L')
    im_bank_0 = image.crop(
        (My_Bank_Pixel_X, My_Bank_Pixel_Y, (My_Bank_Pixel_X + Bank_w), (My_Bank_Pixel_Y + Bank_h))).convert('L')

    im_bank_1 = PIL.ImageOps.invert(im_bank_1)
    im_bank_2 = PIL.ImageOps.invert(im_bank_2)
    im_bank_3 = PIL.ImageOps.invert(im_bank_3)
    im_bank_4 = PIL.ImageOps.invert(im_bank_4)
    im_bank_5 = PIL.ImageOps.invert(im_bank_5)
    im_bank_6 = PIL.ImageOps.invert(im_bank_6)
    im_bank_7 = PIL.ImageOps.invert(im_bank_7)
    im_bank_8 = PIL.ImageOps.invert(im_bank_8)
    im_bank_0 = PIL.ImageOps.invert(im_bank_0)

    b1 = pytesseract.image_to_string(im_bank_1, config='-c tessedit_char_whitelist=$0123456789')
    b2 = pytesseract.image_to_string(im_bank_2, config='-c tessedit_char_whitelist=$0123456789')
    b3 = pytesseract.image_to_string(im_bank_3, config='-c tessedit_char_whitelist=$0123456789')
    b4 = pytesseract.image_to_string(im_bank_4, config='-c tessedit_char_whitelist=$0123456789')
    b5 = pytesseract.image_to_string(im_bank_5, config='-c tessedit_char_whitelist=$0123456789')
    b6 = pytesseract.image_to_string(im_bank_6, config='-c tessedit_char_whitelist=$0123456789')
    b7 = pytesseract.image_to_string(im_bank_7, config='-c tessedit_char_whitelist=$0123456789')
    b8 = pytesseract.image_to_string(im_bank_8, config='-c tessedit_char_whitelist=$0123456789')

    b0 = pytesseract.image_to_string(im_bank_0, config='-c tessedit_char_whitelist=$0123456789')
    Bank_list.append(('Player_0: ' + str(b0).partition('\n')[0]))

    if ('1' in players_list) and not (str(b1) == '\x0c'):
        bank = str(b1).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_1: ' + bank)
    if ('2' in players_list) and not (str(b2) == '\x0c'):
        bank = str(b2).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_2: ' + bank)
    if ('3' in players_list) and not (str(b3) == '\x0c'):
        bank = str(b3).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_3: ' + bank)
    if ('4' in players_list) and not (str(b4) == '\x0c'):
        bank = str(b4).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_4: ' + bank)
    if ('5' in players_list) and not (str(b5) == '\x0c'):
        bank = str(b5).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_5: ' + bank)
    if ('6' in players_list) and not (str(b6) == '\x0c'):
        bank = str(b6).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_6: ' + bank)
    if ('7' in players_list) and not (str(b7) == '\x0c'):
        bank = str(b7).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_7: ' + bank)
    if ('8' in players_list) and not (str(b8) == '\x0c'):
        bank = str(b8).partition('\n')[0]
        if bank == '':
            bank = '0'
        Bank_list.append('Player_8: ' + bank)

    return (str(Bank_list).partition('[')[2].rpartition(']')[0])


def three_button(image_button):
    image = image_button
    white_color_for_getpixel = '(255, 255, 255, 255)'

    if str(image.getpixel((Activator_Pixel_X, Activator_Pixel_Y))) == white_color_for_getpixel:
        if str(image.getpixel((Fold_Button_Pixel_X, Fold_Button_Pixel_Y))) == white_color_for_getpixel:
            return 'fold_call_rise'
        else:
            return 'check_bet'
    else:
        return 'fold_call'


def counting_rates(banks_list1, banks_list2, roles, players, lap):
    Rates = []
    Differnces = []

    if ('Player_1: ' in banks_list1) and ('Player_1: ' in banks_list2):
        try:
            difference1 = int(banks_list1.partition('Player_1: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_1: ')[2].partition("'")[0])
        except:
            difference1 = 0
        Rates.append('Player_1: ' + str(difference1))

    if ('Player_2: ' in banks_list1) and ('Player_2: ' in banks_list2):
        try:
            difference2 = int(banks_list1.partition('Player_2: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_2: ')[2].partition("'")[0])
        except:
            difference2 = 0
        Rates.append('Player_2: ' + str(difference2))

    if ('Player_3: ' in banks_list1) and ('Player_3: ' in banks_list2):
        try:
            difference3 = int(banks_list1.partition('Player_3: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_3: ')[2].partition("'")[0])
        except:
            difference3 = 0
        Rates.append('Player_3: ' + str(difference3))

    if ('Player_4: ' in banks_list1) and ('Player_4: ' in banks_list2):
        try:
            difference4 = int(banks_list1.partition('Player_4: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_4: ')[2].partition("'")[0])
        except:
            difference4 = 0
        Rates.append('Player_4: ' + str(difference4))

    if ('Player_5: ' in banks_list1) and ('Player_5: ' in banks_list2):
        try:
            difference5 = int(banks_list1.partition('Player_5: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_5: ')[2].partition("'")[0])
        except:
            difference5 = 0
        Rates.append('Player_5: ' + str(difference5))

    if ('Player_6: ' in banks_list1) and ('Player_6: ' in banks_list2):
        try:
            difference6 = int(banks_list1.partition('Player_6: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_6: ')[2].partition("'")[0])
        except:
            difference6 = 0
        Rates.append('Player_6: ' + str(difference6))

    if ('Player_7: ' in banks_list1) and ('Player_7: ' in banks_list2):
        try:
            difference7 = int(banks_list1.partition('Player_7: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_7: ')[2].partition("'")[0])
        except:
            difference7 = 0
        Rates.append('Player_7: ' + str(difference7))

    if ('Player_8: ' in banks_list1) and ('Player_8: ' in banks_list2):
        try:
            difference8 = int(banks_list1.partition('Player_8: ')[2].partition("'")[0]) - int(
                banks_list2.partition('Player_8: ')[2].partition("'")[0])
        except:
            difference8 = 0
        Rates.append('Player_8: ' + str(difference8))

    if lap == 1:
        for i in range(int(roles.rpartition(',')[2]), 9):
            if str(i) in players:
                Differnces.append('Player_' + str(i) + ': ' +
                                  str(Rates).partition('[')[2].rpartition(']')[0].partition('er_' + str(i) + ': ')[
                                      2].partition("'")[0])

    else:
        for i in range(1, 9):
            if str(i) in players:
                Differnces.append('Player_' + str(i) + ': ' +
                                  str(Rates).partition('[')[2].rpartition(']')[0].partition('er_' + str(i) + ': ')[
                                      2].partition("'")[0])

    return str(Differnces).partition('[')[2].partition(']')[0]


def end_of_raund(image_input):
    image = image_input
    white_color_for_getpixel = '(255, 255, 255, 255)'

    if str(image.getpixel((Start_Testing_Pixel_X, Start_Testing_Pixel_Y))) == white_color_for_getpixel:
        return False
    else:
        return True


def get_answer():
    pass


def simulator():
    pass


def main():
    # Player_1 = Player(None,None,None,None,None,None,None)
    # Player_2 = Player(None,None,None,None,None,None,None)
    # Player_3 = Player(None,None,None,None,None,None,None)
    # Player_4 = Player(None,None,None,None,None,None,None)
    # Player_5 = Player(None,None,None,None,None,None,None)
    # Player_6 = Player(None,None,None,None,None,None,None)
    # Player_7 = Player(None,None,None,None,None,None,None)
    # Player_8 = Player(None,None,None,None,None,None,None)

    # # waiting_start() # Ждем раздачи карт
    # _1_screenshot = pyautogui.screenshot('1st_ss.png')
    # # Считываем информацию о именах, банках
    # # Записываем их в соответсвующие классы + записываем с кого начинаются торги
    #
    # print(stop_playing()) # Определяет открыто ли меню - для выхода
    #
    # Cards_On_Hands = check_hands_cards(_1_screenshot)
    # Card_Hand_1 = Card('HAND1',Cards_On_Hands.partition(',')[0],Cards_On_Hands.partition(',')[2].partition(';')[0])
    # Card_Hand_2 = Card('HAND2',Cards_On_Hands.partition(';')[2].partition(',')[0],Cards_On_Hands.rpartition(',')[2])
    #
    # print(now_stage(_1_screenshot)) # Определяет этап игры в зависимости от количества карт на столе
    # print(who_is_active(_1_screenshot)) # Какие места за столом заняты
    # print(who_is_playing(_1_screenshot)) # У кого карты на руках еще
    # print(check_hands_cards(_1_screenshot)) # Выдает две карты с рук
    # print(check_table_cards(_1_screenshot)) # Выдает карты со стола
    # print(check_players_banks(_1_screenshot,who_is_playing(_1_screenshot))) # Выдает игроков и их банки
    # print(who_is_starting(_1_screenshot, check_players_banks(_1_screenshot,who_is_playing(_1_screenshot)))) # Определяет трех игроков МБ ББ и кто начинает торги

    while stop_playing() == False:

        End_Of_Raund = False

        waiting_start()  # Ждем раздачи карт
        time.sleep(0.3)

        _1_screenshot = pyautogui.screenshot('1st_ss.png')
        lap = 1

        Cards_On_Hands = check_hands_cards(_1_screenshot)
        Card_Hand_1 = Card('HAND1', Cards_On_Hands.partition(',')[0],
                           Cards_On_Hands.partition(',')[2].partition(';')[0])
        Card_Hand_2 = Card('HAND2', Cards_On_Hands.partition(';')[2].partition(',')[0],
                           Cards_On_Hands.rpartition(',')[2])

        Players_Banks = check_players_banks(_1_screenshot, who_is_playing(
            _1_screenshot))  # Переменные для дальнейшего определения элементов
        Players_Active = who_is_playing(_1_screenshot)
        Player_Role = who_is_starting(_1_screenshot, Players_Banks)
        if True:  # Заполнение 8 элементов класса Player
            if 'Player_1' in Players_Banks:
                if '1' in Players_Active:
                    if '1' in Player_Role:
                        if Player_Role.partition(',')[0] == '1':
                            Player_1 = Player('Player1', int(Players_Banks.partition('_1: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '1':
                            Player_1 = Player('Player1', int(Players_Banks.partition('_1: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '1':
                            Player_1 = Player('Player1', int(Players_Banks.partition('_1: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_1 = Player('Player1', int(Players_Banks.partition('_1: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_1 = Player('Player1', None,
                                  None, None, 0, 0, None)

            if 'Player_2' in Players_Banks:
                if '2' in Players_Active:
                    if '2' in Player_Role:
                        if Player_Role.partition(',')[0] == '2':
                            Player_2 = Player('Player2', int(Players_Banks.partition('_2: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '2':
                            Player_2 = Player('Player2', int(Players_Banks.partition('_2: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '2':
                            Player_2 = Player('Player2', int(Players_Banks.partition('_2: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_2 = Player('Player2', int(Players_Banks.partition('_2: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_2 = Player('Player2', None,
                                  None, None, 0, 0, None)

            if 'Player_3' in Players_Banks:
                if '3' in Players_Active:
                    if '3' in Player_Role:
                        if Player_Role.partition(',')[0] == '3':
                            Player_3 = Player('Player3', int(Players_Banks.partition('_3: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '3':
                            Player_3 = Player('Player3', int(Players_Banks.partition('_3: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '3':
                            Player_3 = Player('Player3', int(Players_Banks.partition('_3: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_3 = Player('Player3', int(Players_Banks.partition('_3: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_3 = Player('Player3', None,
                                  None, None, 0, 0, None)

            if 'Player_4' in Players_Banks:
                if '4' in Players_Active:
                    if '4' in Player_Role:
                        if Player_Role.partition(',')[0] == '4':
                            Player_4 = Player('Player4', int(Players_Banks.partition('_4: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '4':
                            Player_4 = Player('Player4', int(Players_Banks.partition('_4: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '4':
                            Player_4 = Player('Player4', int(Players_Banks.partition('_4: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_4 = Player('Player4', int(Players_Banks.partition('_4: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_4 = Player('Player4', None,
                                  None, None, 0, 0, None)

            if 'Player_5' in Players_Banks:
                if '5' in Players_Active:
                    if '5' in Player_Role:
                        if Player_Role.partition(',')[0] == '5':
                            Player_5 = Player('Player5', int(Players_Banks.partition('_5: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '5':
                            Player_5 = Player('Player5', int(Players_Banks.partition('_5: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '5':
                            Player_5 = Player('Player5', int(Players_Banks.partition('_5: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_5 = Player('Player5', int(Players_Banks.partition('_5: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_5 = Player('Player5', None,
                                  None, None, 0, 0, None)

            if 'Player_6' in Players_Banks:
                if '6' in Players_Active:
                    if '6' in Player_Role:
                        if Player_Role.partition(',')[0] == '6':
                            Player_6 = Player('Player6', int(Players_Banks.partition('_6: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '6':
                            Player_6 = Player('Player6', int(Players_Banks.partition('_6: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '6':
                            Player_6 = Player('Player6', int(Players_Banks.partition('_6: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_6 = Player('Player6', int(Players_Banks.partition('_6: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_6 = Player('Player6', None,
                                  None, None, 0, 0, None)

            if 'Player_7' in Players_Banks:
                if '7' in Players_Active:
                    if '7' in Player_Role:
                        if Player_Role.partition(',')[0] == '7':
                            Player_7 = Player('Player7', int(Players_Banks.partition('_7: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '7':
                            Player_7 = Player('Player7', int(Players_Banks.partition('_7: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '7':
                            Player_7 = Player('Player7', int(Players_Banks.partition('_7: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_7 = Player('Player7', int(Players_Banks.partition('_7: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_7 = Player('Player7', None,
                                  None, None, 0, 0, None)

            if 'Player_8' in Players_Banks:
                if '8' in Players_Active:
                    if '8' in Player_Role:
                        if Player_Role.partition(',')[0] == '8':
                            Player_8 = Player('Player8', int(Players_Banks.partition('_8: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'MB')
                        if Player_Role.partition(', ')[2].rpartition(',')[0] == '8':
                            Player_8 = Player('Player8', int(Players_Banks.partition('_8: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'BB')
                        if Player_Role.rpartition(', ')[2] == '8':
                            Player_8 = Player('Player8', int(Players_Banks.partition('_8: ')[2].partition("'")[0]),
                                              'ON', 'TRUE', 0, 0, 'ST')
                    else:
                        Player_8 = Player('Player8', int(Players_Banks.partition('_8: ')[2].partition("'")[0]),
                                          'ON', 'TRUE', 0, 0, None)
            else:
                Player_8 = Player('Player8', None,
                                  None, None, 0, 0, None)  # #

        My_Bank_1 = Players_Banks.partition('_0: ')[2].partition("'")[0]
        if '0' in Player_Role:
            if Player_Role.partition(',')[0] == '0':
                My_Role = 'MB'
            if Player_Role.partition(', ')[2].rpartition(',')[0] == '0':
                My_Role = 'BB'
            if Player_Role.rpartition(',')[2] == '0':
                My_Role = 'ST'

        os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/1st_ss.png')

        waiting_my_turn()
        main_screenshot = pyautogui.screenshot('main_ss.png')

        lap = 1
        while now_stage(main_screenshot) == 1 and End_Of_Raund == False:
            if lap == 1:
                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)

                Table_Cards = check_table_cards(main_screenshot)
                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])))
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])))
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])))
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])))
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])))
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])))
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])))
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])))
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ В РУКЕ: ' + Cards_On_Hands)
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)
                # Нужно подсчитать ставки игроков за круг и за кон + карты на столе + роли( первый псоле мб начинает)
                lap = lap + 1

            else:

                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)

                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])))
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])))
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])))
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])))
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])))
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])))
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])))
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])))
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks_2))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)

                lap = lap + 1

            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/main_ss.png')

            test_end_ss = pyautogui.screenshot('end_test_ss.png')
            End_Of_Raund = end_of_raund(test_end_ss)
            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/end_test_ss.png')

            time.sleep(2)

            if End_Of_Raund == False:
                waiting_my_turn()
                main_screenshot = pyautogui.screenshot('main_ss.png')

        Players_Banks = Players_Banks_2

        lap = 1
        while now_stage(main_screenshot) == 2 and End_Of_Raund == False:
            if lap == 1:
                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)
                Table_Cards = check_table_cards(main_screenshot)
                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])) - Player_1.sum_bet)
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])) - Player_2.sum_bet)
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])) - Player_3.sum_bet)
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])) - Player_4.sum_bet)
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])) - Player_5.sum_bet)
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])) - Player_6.sum_bet)
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])) - Player_7.sum_bet)
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])) - Player_8.sum_bet)
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ В РУКЕ: ' + Cards_On_Hands)
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)
                # Нужно подсчитать ставки игроков за круг и за кон + карты на столе + роли( первый псоле мб начинает)
                lap = lap + 1
            else:
                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)

                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])) - Player_1.sum_bet)
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])) - Player_2.sum_bet)
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])) - Player_3.sum_bet)
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])) - Player_4.sum_bet)
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])) - Player_5.sum_bet)
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])) - Player_6.sum_bet)
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])) - Player_7.sum_bet)
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])) - Player_8.sum_bet)
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks_2))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)

                lap = lap + 1

            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/main_ss.png')

            test_end_ss = pyautogui.screenshot('end_test_ss.png')
            End_Of_Raund = end_of_raund(test_end_ss)
            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/end_test_ss.png')
            time.sleep(2)
            if End_Of_Raund == False:
                waiting_my_turn()
                main_screenshot = pyautogui.screenshot('main_ss.png')

        Players_Banks = Players_Banks_2

        lap = 1
        while now_stage(main_screenshot) == 3 and End_Of_Raund == False:
            if lap == 1:
                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)
                Table_Cards = check_table_cards(main_screenshot)
                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])) - Player_1.sum_bet)
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])) - Player_2.sum_bet)
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])) - Player_3.sum_bet)
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])) - Player_4.sum_bet)
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])) - Player_5.sum_bet)
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])) - Player_6.sum_bet)
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])) - Player_7.sum_bet)
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])) - Player_8.sum_bet)
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ В РУКЕ: ' + Cards_On_Hands)
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)
                # Нужно подсчитать ставки игроков за круг и за кон + карты на столе + роли( первый псоле мб начинает)
                lap = lap + 1
            else:
                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)

                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])) - Player_1.sum_bet)
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])) - Player_2.sum_bet)
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])) - Player_3.sum_bet)
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])) - Player_4.sum_bet)
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])) - Player_5.sum_bet)
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])) - Player_6.sum_bet)
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])) - Player_7.sum_bet)
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])) - Player_8.sum_bet)
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks_2))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)

                lap = lap + 1

            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/main_ss.png')

            test_end_ss = pyautogui.screenshot('end_test_ss.png')
            End_Of_Raund = end_of_raund(test_end_ss)
            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/end_test_ss.png')
            time.sleep(2)
            if End_Of_Raund == False:
                waiting_my_turn()
                main_screenshot = pyautogui.screenshot('main_ss.png')

        Players_Banks = Players_Banks_2

        lap = 1
        while now_stage(main_screenshot) == 4 and End_Of_Raund == False:
            if lap == 1:
                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)
                Table_Cards = check_table_cards(main_screenshot)
                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])) - Player_1.sum_bet)
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])) - Player_2.sum_bet)
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])) - Player_3.sum_bet)
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])) - Player_4.sum_bet)
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])) - Player_5.sum_bet)
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])) - Player_6.sum_bet)
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])) - Player_7.sum_bet)
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])) - Player_8.sum_bet)
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ В РУКЕ: ' + Cards_On_Hands)
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)
                # Нужно подсчитать ставки игроков за круг и за кон + карты на столе + роли( первый псоле мб начинает)
                lap = lap + 1
            else:
                Players_Banks_2 = check_players_banks(main_screenshot, who_is_active(main_screenshot))
                Roles = who_is_starting(main_screenshot, Players_Banks_2)
                Buttons = three_button(main_screenshot)
                Rates = counting_rates(Players_Banks, Players_Banks_2,
                                       who_is_starting(main_screenshot, Players_Banks_2),
                                       who_is_active(main_screenshot), lap)

                if '_1: ' in Rates:
                    Player_1.new_actual_bet((int(Rates.partition('1: ')[2].partition("'")[0])) - Player_1.sum_bet)
                    Player_1.nem_sum_bet((Player_1.actual_bet + Player_1.sum_bet))
                if '_2: ' in Rates:
                    Player_2.new_actual_bet((int(Rates.partition('2: ')[2].partition("'")[0])) - Player_2.sum_bet)
                    Player_2.nem_sum_bet((Player_2.actual_bet + Player_2.sum_bet))
                if '_3: ' in Rates:
                    Player_3.new_actual_bet((int(Rates.partition('3: ')[2].partition("'")[0])) - Player_3.sum_bet)
                    Player_3.nem_sum_bet((Player_3.actual_bet + Player_3.sum_bet))
                if '_4: ' in Rates:
                    Player_4.new_actual_bet((int(Rates.partition('4: ')[2].partition("'")[0])) - Player_4.sum_bet)
                    Player_4.nem_sum_bet((Player_4.actual_bet + Player_4.sum_bet))
                if '_5: ' in Rates:
                    Player_5.new_actual_bet((int(Rates.partition('5: ')[2].partition("'")[0])) - Player_5.sum_bet)
                    Player_5.nem_sum_bet((Player_5.actual_bet + Player_5.sum_bet))
                if '_6: ' in Rates:
                    Player_6.new_actual_bet((int(Rates.partition('6: ')[2].partition("'")[0])) - Player_6.sum_bet)
                    Player_6.nem_sum_bet((Player_6.actual_bet + Player_6.sum_bet))
                if '_7: ' in Rates:
                    Player_7.new_actual_bet((int(Rates.partition('7: ')[2].partition("'")[0])) - Player_7.sum_bet)
                    Player_7.nem_sum_bet((Player_7.actual_bet + Player_7.sum_bet))
                if '_8: ' in Rates:
                    Player_8.new_actual_bet((int(Rates.partition('8: ')[2].partition("'")[0])) - Player_8.sum_bet)
                    Player_8.nem_sum_bet((Player_8.actual_bet + Player_8.sum_bet))

                print('************ круг: ' + str(lap) + ', этап игры: ' + str(now_stage(main_screenshot)))
                print('БАНКИ ИГРОКОВ: ' + str(Players_Banks_2))
                print('РОЛИ: ' + str(Roles))
                print('КНОПКИ: ' + str(Buttons))
                print('СТАВКИ: ' + str(Rates))
                print('КАРТЫ НА СТОЛЕ: ' + Table_Cards)

                lap = lap + 1

            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/main_ss.png')
            time.sleep(2)
            test_end_ss = pyautogui.screenshot('end_test_ss.png')
            End_Of_Raund = end_of_raund(test_end_ss)
            os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/end_test_ss.png')

            if End_Of_Raund == False:
                waiting_my_turn()
                main_screenshot = pyautogui.screenshot('main_ss.png')

        Players_Banks = Players_Banks_2

        # Players_Banks_2 = check_players_banks(_2_screenshot, who_is_playing(_2_screenshot))
        # print(Players_Banks)
        # print(Players_Banks_2)
        # print(who_is_starting(_2_screenshot,Players_Banks_2))
        # print(who_is_active(_2_screenshot))
        # print(counting_rates(Players_Banks,Players_Banks_2,who_is_starting(_2_screenshot, Players_Banks_2),who_is_active(_2_screenshot),lap))
        #
        # print('КАРТЫ В РУКЕ:')
        # print(Cards_On_Hands)
        # print('БАНК ИГРОКА 1:')
        # print(Player_1.bank)
        # print('РОЛЬ ИГРОКА 6:')
        # print(Player_6.role)
        # print('РОЛЬ ИГРОКА 3:')
        # print(Player_1.role)
        # print('МОЙ БАНК:')
        # print(My_Bank_1)
        # print(three_button(_2_screenshot))
        # print(Player_8.role)
        # get_answer()
        # simulator(three_button(_2_screenshot), get_answer())
        # os.remove('/Users/vlad/PycharmProjects/PokerMaster/venv/2nd_ss.png')
        #
        # waiting_my_turn()
        #
        # _3_screenshot = pyautogui.screenshot('3rd_sss.png')
        #
        # if now_stage(_3_screenshot) == 1:
        #     while (now_stage(_3_screenshot) == 1):


main()
