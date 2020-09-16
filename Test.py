import pyautogui
import time

time.sleep(3)

# БЛОК КОНСТАНТ

if True:
    WHITE_COLOR = 'RGB(red=255, green=255, blue=255)'

    Start_Testing_Pixel_X = 577
    Start_Testing_Pixel_Y = 500

    Stop_Pixel_X = 50
    Stop_Pixel_Y = 50
    Color_for_stop = 'RGB(red=219, green=219, blue=220)'

    Activator_Pixel_X = 900
    Activator_Pixel_Y = 700

    Three_Cards_Pixel_X = 579
    Three_Cards_Pixel_Y = 267

    Four_Cards_Pixel_X = 730
    Four_Cards_Pixel_Y = 267

    Five_Cards_Pixel_X = 809
    Five_Cards_Pixel_Y = 267

    Player_1_Testing_Pixel_X = 218
    Player_1_Testing_Pixel_Y = 523
    Color_Of_Absence_Player_1 = 'RGB(red=26, green=28, blue=38)'
    Player_1_Activity_Pixel_X = 234
    Player_1_Activity_Pixel_Y = 461
    Player_1_Timing_Pixel_X = 236
    Player_1_Timing_Pixel_Y = 551
    Player_1_Presence_Of_Label_Pixel_X = 362
    Player_1_Presence_Of_Label_Pixel_Y = 400
    Player_1_Bet_Pixel_X = 410
    Player_1_Bet_Pixel_Y = 418

    Player_2_Testing_Pixel_X = 110
    Player_2_Testing_Pixel_Y = 359
    Color_Of_Absence_Player_2 = 'RGB(red=38, green=40, blue=52)'
    Player_2_Activity_Pixel_X = 120
    Player_2_Activity_Pixel_Y = 302
    Player_2_Timing_Pixel_X = 122
    Player_2_Timing_Pixel_Y = 388
    Player_2_Presence_Of_Label_Pixel_X = 291
    Player_2_Presence_Of_Label_Pixel_Y = 287
    Player_2_Bet_Pixel_X =
    Player_2_Bet_Pixel_Y =

    Player_3_Testing_Pixel_X = 159
    Player_3_Testing_Pixel_Y = 200
    Color_Of_Absence_Player_3 = 'RGB(red=44, green=44, blue=56)'
    Player_3_Activity_Pixel_X = 168
    Player_3_Activity_Pixel_Y = 144
    Player_3_Timing_Pixel_X = 172
    Player_3_Timing_Pixel_Y = 228
    Player_3_Presence_Of_Label_Pixel_X = 420
    Player_3_Presence_Of_Label_Pixel_Y = 215
    Player_3_Bet_Pixel_X = 365
    Player_3_Bet_Pixel_Y = 237

    8 84 24
    6 66 20У

    Player_4_Testing_Pixel_X = 372
    Player_4_Testing_Pixel_Y = 119
    Color_Of_Absence_Player_4 = 'RGB(red=46, green=48, blue=61)'
    Player_4_Activity_Pixel_X = 381
    Player_4_Activity_Pixel_Y = 63
    Player_4_Timing_Pixel_X = 383
    Player_4_Timing_Pixel_Y = 152
    Player_4_Presence_Of_Label_Pixel_X = 603
    Player_4_Presence_Of_Label_Pixel_Y = 163
    Player_4_Bet_Pixel_X =
    Player_4_Bet_Pixel_Y =

    Player_5_Testing_Pixel_X = 906
    Player_5_Testing_Pixel_Y = 124
    Color_Of_Absence_Player_5 = 'RGB(red=47, green=47, blue=49)'
    Player_5_Activity_Pixel_X = 761
    Player_5_Activity_Pixel_Y = 60
    Player_5_Timing_Pixel_X = 766
    Player_5_Timing_Pixel_Y = 153
    Player_5_Presence_Of_Label_Pixel_X = 830
    Player_5_Presence_Of_Label_Pixel_Y = 184
    Player_5_Bet_Pixel_X =
    Player_5_Bet_Pixel_Y =

    Player_6_Testing_Pixel_X = 1119
    Player_6_Testing_Pixel_Y = 201
    Color_Of_Absence_Player_6 = 'RGB(red=44, green=44, blue=46)'
    Player_6_Activity_Pixel_X = 974
    Player_6_Activity_Pixel_Y = 138
    Player_6_Timing_Pixel_X = 979
    Player_6_Timing_Pixel_Y = 230
    Player_6_Presence_Of_Label_Pixel_X = 949
    Player_6_Presence_Of_Label_Pixel_Y = 244
    Player_6_Bet_Pixel_X =
    Player_6_Bet_Pixel_Y =

    Player_7_Testing_Pixel_X = 1196
    Player_7_Testing_Pixel_Y = 338
    Color_Of_Absence_Player_7 = 'RGB(red=38, green=38, blue=40)'
    Player_7_Activity_Pixel = pyautogui.pixel(1022, 296)
    Player_7_Activity_Pixel_X = 1022
    Player_7_Activity_Pixel_Y = 296
    Player_7_Timing_Pixel_X = 1026
    Player_7_Timing_Pixel_Y = 388
    Player_7_Presence_Of_Label_Pixel_X = 986
    Player_7_Presence_Of_Label_Pixel_Y = 396
    Player_7_Bet_Pixel_X =
    Player_7_Bet_Pixel_Y =

    Player_8_Testing_Pixel_X = 1063
    Player_8_Testing_Pixel_Y = 526
    Color_Of_Absence_Player_8 = 'RGB(red=27, green=26, blue=30)'
    Player_8_Activity_Pixel_X = 908
    Player_8_Activity_Pixel_Y = 457
    Player_8_Timing_Pixel_X = 912
    Player_8_Timing_Pixel_Y = 553
    Player_8_Presence_Of_Label_Pixel_X = 852
    Player_8_Presence_Of_Label_Pixel_Y = 455
    Player_8_Bet_Pixel_X =
    Player_8_Bet_Pixel_Y =

# ОПИСАНИЕ КЛАССОВ

class Player:
    def __init__(self, serial_number, Player_Testing_Pixel_X, Player_Testing_Pixel_Y, Color_Of_Absence_Player, Player_Activity_Pixel_X, Player_Activity_Pixel_Y, Player_Timing_Pixel_X, Player_Timing_Pixel_Y, Player_Presence_Of_Label_Pixel_X, Player_Presence_Of_Label_Pixel_Y, name, bank):
        self.number = serial_number
        self.presence_pixel_X = Player_Testing_Pixel_X
        self.presence_pixel_Y = Player_Testing_Pixel_Y
        self.presence_color = Color_Of_Absence_Player
        self.activity_pixel_X = Player_Activity_Pixel_X
        self.activity_pixel_Y = Player_Activity_Pixel_Y
        self.timing_pixel_X = Player_Timing_Pixel_X
        self.timing_pixel_Y = Player_Timing_Pixel_Y
        self.label_pixel_X = Player_Presence_Of_Label_Pixel_X
        self.label_pixel_Y = Player_Presence_Of_Label_Pixel_Y
        self.name = name
        self.bank = bank

    def is_present(self):
        if str(pyautogui.pixel(self.presence_pixel_X,self.presence_pixel_Y)) != self.presence_color:
            return (True)
        else:
            return (False)

    def is_participates(self):
        if str(pyautogui.pixel(self.activity_pixel_X,self.activity_pixel_Y)) == WHITE_COLOR :
            return (True)
        else:
            return (False)

    def turn(self):
        if str(pyautogui.pixel(self.timing_pixel_X,self.timing_pixel_Y)).rpartition(' ')[2].rpartition(')')[0] == 'blue=0':
            return (True)
        else:
            return (False)

    def role(self):
        if int(str(pyautogui.pixel(self.label_pixel_X,self.label_pixel_Y)).rpartition('=')[2].rpartition(')')[0]) >= 200:
            return (True)
        else:
            return (False)

    def number(self):
        return self.number()

    def name(self):
        return self.name()

    def bank(self):
        return self.bank()

# ОСНОВНЫЕ ФУНКЦИИ

def now_stage(): #Определение количесвта карт на столе
    if str(pyautogui.pixel(Three_Cards_Pixel_X,Three_Cards_Pixel_Y)) == WHITE_COLOR:
        if str(pyautogui.pixel(Four_Cards_Pixel_X,Four_Cards_Pixel_Y)) == WHITE_COLOR:
            if str(pyautogui.pixel(Five_Cards_Pixel_X,Five_Cards_Pixel_Y)) == WHITE_COLOR:
                return 4
            else:
                return 3
        else:
            return 2
    else:
        return 1

def stop_playing(): #Программа прекращает работу при открытии вкладки СТОЛ
    if str(pyautogui.pixel(Stop_Pixel_X,Stop_Pixel_Y)) == Color_for_stop:
        return True
    else:
        return False

def waiting_start(): #Ожидание пока карты придут в руку

    def start_playing():  # Определяет наличие карт на руках
        if str(pyautogui.pixel(Start_Testing_Pixel_X, Start_Testing_Pixel_Y)) == WHITE_COLOR:
            return True
        else:
            return False

    i=0
    while i == 0:
        if start_playing() == True:
            i=1

def waiting_my_turn():
    def my_move():
        if str(pyautogui.pixel(Activator_Pixel_X, Activator_Pixel_Y)) == WHITE_COLOR:
            return True
        else:
            return False

    i = 0
    while i == 0:
        if my_move() == True:
            i = 1

def bet_check_1st_lap(b): #Возвращает номера игроков и их ставки
    if 1>=b:


def bet_check_other_laps(): #Возвращает номера игроков и их поднятые ставки
    pass

def check_for(p1,p2,p3,p4,p5,p6,p7,p8): #Опредление выборки среди игроков
    Numbers_Of_Players = []
    if p1 == True:
        Numbers_Of_Players.append(1)
    if p2 == True:
        Numbers_Of_Players.append(2)
    if p3 == True:
        Numbers_Of_Players.append(3)
    if p4 == True:
        Numbers_Of_Players.append(4)
    if p5 == True:
        Numbers_Of_Players.append(5)
    if p6 == True:
        Numbers_Of_Players.append(6)
    if p7 == True:
        Numbers_Of_Players.append(7)
    if p8 == True:
        Numbers_Of_Players.append(8)

    return Numbers_Of_Players

# ГЛАВНАЯ ФУНКЦИЯ

def main():
    if True:
        player_1 = Player(1, Player_1_Testing_Pixel_X, Player_1_Testing_Pixel_Y, Color_Of_Absence_Player_1,
                          Player_1_Activity_Pixel_X, Player_1_Activity_Pixel_Y, Player_1_Timing_Pixel_X,
                          Player_1_Timing_Pixel_Y, Player_1_Presence_Of_Label_Pixel_X,
                          Player_1_Presence_Of_Label_Pixel_Y,
                          'NAME1', 'BANK1')
        player_2 = Player(2, Player_2_Testing_Pixel_X, Player_2_Testing_Pixel_Y, Color_Of_Absence_Player_2,
                          Player_2_Activity_Pixel_X, Player_2_Activity_Pixel_Y, Player_2_Timing_Pixel_X,
                          Player_2_Timing_Pixel_Y, Player_2_Presence_Of_Label_Pixel_X,
                          Player_2_Presence_Of_Label_Pixel_Y,
                          'NAME2', 'BANK2')
        player_3 = Player(3, Player_3_Testing_Pixel_X, Player_3_Testing_Pixel_Y, Color_Of_Absence_Player_3,
                          Player_3_Activity_Pixel_X, Player_3_Activity_Pixel_Y, Player_3_Timing_Pixel_X,
                          Player_3_Timing_Pixel_Y, Player_3_Presence_Of_Label_Pixel_X,
                          Player_3_Presence_Of_Label_Pixel_Y,
                          'NAME3', 'BANK3')
        player_4 = Player(4, Player_4_Testing_Pixel_X, Player_4_Testing_Pixel_Y, Color_Of_Absence_Player_4,
                          Player_4_Activity_Pixel_X, Player_4_Activity_Pixel_Y, Player_4_Timing_Pixel_X,
                          Player_4_Timing_Pixel_Y, Player_4_Presence_Of_Label_Pixel_X,
                          Player_4_Presence_Of_Label_Pixel_Y,
                          'NAME4', 'BANK4')
        player_5 = Player(5, Player_5_Testing_Pixel_X, Player_5_Testing_Pixel_Y, Color_Of_Absence_Player_5,
                          Player_5_Activity_Pixel_X, Player_5_Activity_Pixel_Y, Player_5_Timing_Pixel_X,
                          Player_5_Timing_Pixel_Y, Player_5_Presence_Of_Label_Pixel_X,
                          Player_5_Presence_Of_Label_Pixel_Y,
                          'NAME5', 'BANK5')
        player_6 = Player(6, Player_6_Testing_Pixel_X, Player_6_Testing_Pixel_Y, Color_Of_Absence_Player_6,
                          Player_6_Activity_Pixel_X, Player_6_Activity_Pixel_Y, Player_6_Timing_Pixel_X,
                          Player_6_Timing_Pixel_Y, Player_6_Presence_Of_Label_Pixel_X,
                          Player_6_Presence_Of_Label_Pixel_Y,
                          'NAME6', 'BANK6')
        player_7 = Player(7, Player_7_Testing_Pixel_X, Player_7_Testing_Pixel_Y, Color_Of_Absence_Player_7,
                          Player_7_Activity_Pixel_X, Player_7_Activity_Pixel_Y, Player_7_Timing_Pixel_X,
                          Player_7_Timing_Pixel_Y, Player_7_Presence_Of_Label_Pixel_X,
                          Player_7_Presence_Of_Label_Pixel_Y,
                          'NAME7', 'BANK7')
        player_8 = Player(8, Player_8_Testing_Pixel_X, Player_8_Testing_Pixel_Y, Color_Of_Absence_Player_8,
                          Player_8_Activity_Pixel_X, Player_8_Activity_Pixel_Y, Player_8_Timing_Pixel_X,
                          Player_8_Timing_Pixel_Y, Player_8_Presence_Of_Label_Pixel_X,
                          Player_8_Presence_Of_Label_Pixel_Y,
                          'NAME8', 'BANK8')

    try:
        while stop_playing() == False:
            waiting_start()
            waiting_my_turn()

            b = check_for(player_1.role(),player_2.role(),player_3.role(),player_4.role(),player_5.role(),player_6.role(),player_7.role(),player_8.role())
            b = int(str(b).partition('[')[2].rpartition(']')[0])+1

            if now_stage() == 1:
                bet_check_1st_lap(b)
                while now_stage() == 1:
                    bet_check_other_laps()
            if now_stage() == 2:
                pass
            if now_stage() == 3:
                pass
            if now_stage() == 4:
                pass


            # a = check_for(player_1.is_present(), player_2.is_present(), player_3.is_present(), player_4.is_present(),
            #               player_5.is_present(), player_6.is_present(), player_7.is_present(), player_8.is_present())
            # print('Учавствуют игроки: ' + str(a).partition('[')[2].rpartition(']')[0])
            #
            b = check_for(player_1.role(),player_2.role(),player_3.role(),player_4.role(),player_5.role(),player_6.role(),player_7.role(),player_8.role())
            print('Торги начинаются с игрока: ' + str(int(str(b).partition('[')[2].rpartition(']')[0])+1))
    except:
        print('ERROR IN MAIN')


main()
