# ui.py - functions and main
import tkinter as tk
import random
from parameters import *

# change turn
def change():
    global turn
    turn = (turn + 1) % 3

# convert string to color
def trans(color):
    if color == 'green':
        return green_
    if color == 'gray':
        return gray_
    if color == 'blue':
        return blue_
    if color == 'black':
        return black_
    if color == 'red':
        return red_
    if color == 'gold':
        return gold_

# print and update nobles

def Noble1_print(window, num):
    noble1.green = Noble[num]['green']
    noble1.gray = Noble[num]['gray']
    noble1.blue = Noble[num]['blue']
    noble1.black = Noble[num]['black']
    noble1.red = Noble[num]['red']
    space = 20
    start = 140
    tk.Label(window, text=3, fg='black', font=('PingHei', 16, "bold")).place(x=156, y=146, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['green'])+' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['gray'])+' ', fg=gray_, font=('PingHei', 15, "bold")).place(x=start + space, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['blue'])+' ', fg=blue_, font=('PingHei', 15, "bold")).place(x=start + space * 2, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['black'])+' ', fg=black_, font=('PingHei', 15, "bold")).place(x=start + space * 3, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['red'])+' ', fg=red_, font=('PingHei', 15, "bold")).place(x=start + space * 4, y=187, anchor='nw')

def Noble2_print(window, num):
    noble2.green = Noble[num]['green']
    noble2.gray = Noble[num]['gray']
    noble2.blue = Noble[num]['blue']
    noble2.black = Noble[num]['black']
    noble2.red = Noble[num]['red']
    space = 20
    start = 308
    tk.Label(window, text=3, fg='black', font=('PingHei', 16, "bold")).place(x=325, y=146, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['green'])+' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['gray'])+' ', fg=gray_, font=('PingHei', 15, "bold")).place(x=start + space, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['blue'])+' ', fg=blue_, font=('PingHei', 15, "bold")).place(x=start + space * 2, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['black'])+' ', fg=black_, font=('PingHei', 15, "bold")).place(x=start + space * 3, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['red'])+' ', fg=red_, font=('PingHei', 15, "bold")).place(x=start + space * 4, y=187, anchor='nw')

def Noble3_print(window, num):
    noble3.green = Noble[num]['green']
    noble3.gray = Noble[num]['gray']
    noble3.blue = Noble[num]['blue']
    noble3.black = Noble[num]['black']
    noble3.red = Noble[num]['red']
    space = 20
    start = 468
    tk.Label(window, text=3, fg='black', font=('PingHei', 16, "bold")).place(x=485, y=146, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['green'])+' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['gray'])+' ', fg=gray_, font=('PingHei', 15, "bold")).place(x=start + space, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['blue'])+' ', fg=blue_, font=('PingHei', 15, "bold")).place(x=start + space * 2, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['black'])+' ', fg=black_, font=('PingHei', 15, "bold")).place(x=start + space * 3, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['red'])+' ', fg=red_, font=('PingHei', 15, "bold")).place(x=start + space * 4, y=187, anchor='nw')

def Noble4_print(window, num):
    noble4.green = Noble[num]['green']
    noble4.gray = Noble[num]['gray']
    noble4.blue = Noble[num]['blue']
    noble4.black = Noble[num]['black']
    noble4.red = Noble[num]['red']
    space = 20
    start = 629
    tk.Label(window, text=3, fg='black', font=('PingHei', 16, "bold")).place(x=645, y=146, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['green'])+' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['gray'])+' ', fg=gray_, font=('PingHei', 15, "bold")).place(x=start + space, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['blue'])+' ', fg=blue_, font=('PingHei', 15, "bold")).place(x=start + space * 2, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['black'])+' ', fg=black_, font=('PingHei', 15, "bold")).place(x=start + space * 3, y=187, anchor='nw')
    tk.Label(window, text=' '+str(Noble[num]['red'])+' ', fg=red_, font=('PingHei', 15, "bold")).place(x=start + space * 4, y=187, anchor='nw')

# print and update cards

def Card3_1_print(window, num):
    card31.score = Card3[num]['score']
    card31.bonus = Card3[num]['bonus']
    card31.green = Card3[num]['green']
    card31.gray = Card3[num]['gray']
    card31.blue = Card3[num]['blue']
    card31.black = Card3[num]['black']
    card31.red = Card3[num]['red']
    space = 20
    start = 140
    y = 342
    score_x = 156
    score_place = 55
    tk.Label(window, text=Card3[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card3[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card3_2_print(window, num):
    card32.score = Card3[num]['score']
    card32.bonus = Card3[num]['bonus']
    card32.green = Card3[num]['green']
    card32.gray = Card3[num]['gray']
    card32.blue = Card3[num]['blue']
    card32.black = Card3[num]['black']
    card32.red = Card3[num]['red']
    space = 20
    start = 308
    y = 342
    score_x = 325
    score_place = 55
    tk.Label(window, text=Card3[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card3[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card3_3_print(window, num):
    card33.score = Card3[num]['score']
    card33.bonus = Card3[num]['bonus']
    card33.green = Card3[num]['green']
    card33.gray = Card3[num]['gray']
    card33.blue = Card3[num]['blue']
    card33.black = Card3[num]['black']
    card33.red = Card3[num]['red']
    space = 20
    start = 468
    y = 342
    score_x = 485
    score_place = 55
    tk.Label(window, text=Card3[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card3[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card3_4_print(window, num):
    card34.score = Card3[num]['score']
    card34.bonus = Card3[num]['bonus']
    card34.green = Card3[num]['green']
    card34.gray = Card3[num]['gray']
    card34.blue = Card3[num]['blue']
    card34.black = Card3[num]['black']
    card34.red = Card3[num]['red']
    space = 20
    start = 629
    y = 342
    score_x = 645
    score_place = 55
    tk.Label(window, text=Card3[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card3[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card3[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card2_1_print(window, num):
    card21.score = Card2[num]['score']
    card21.bonus = Card2[num]['bonus']
    card21.green = Card2[num]['green']
    card21.gray = Card2[num]['gray']
    card21.blue = Card2[num]['blue']
    card21.black = Card2[num]['black']
    card21.red = Card2[num]['red']
    space = 20
    start = 140
    y = 493
    score_x = 156
    score_place = 55
    tk.Label(window, text=Card2[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card2[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card2_2_print(window, num):
    card22.score = Card2[num]['score']
    card22.bonus = Card2[num]['bonus']
    card22.green = Card2[num]['green']
    card22.gray = Card2[num]['gray']
    card22.blue = Card2[num]['blue']
    card22.black = Card2[num]['black']
    card22.red = Card2[num]['red']
    space = 20
    start = 308
    y = 493
    score_x = 325
    score_place = 55
    tk.Label(window, text=Card2[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card2[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card2_3_print(window, num):
    card23.score = Card2[num]['score']
    card23.bonus = Card2[num]['bonus']
    card23.green = Card2[num]['green']
    card23.gray = Card2[num]['gray']
    card23.blue = Card2[num]['blue']
    card23.black = Card2[num]['black']
    card23.red = Card2[num]['red']
    space = 20
    start = 468
    y = 493
    score_x = 485
    score_place = 55
    tk.Label(window, text=Card2[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card2[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card2_4_print(window, num):
    card24.score = Card2[num]['score']
    card24.bonus = Card2[num]['bonus']
    card24.green = Card2[num]['green']
    card24.gray = Card2[num]['gray']
    card24.blue = Card2[num]['blue']
    card24.black = Card2[num]['black']
    card24.red = Card2[num]['red']
    space = 20
    start = 629
    y = 493
    score_x = 645
    score_place = 55
    tk.Label(window, text=Card2[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card2[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card2[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card1_1_print(window, num):
    card11.score = Card1[num]['score']
    card11.bonus = Card1[num]['bonus']
    card11.green = Card1[num]['green']
    card11.gray = Card1[num]['gray']
    card11.blue = Card1[num]['blue']
    card11.black = Card1[num]['black']
    card11.red = Card1[num]['red']
    space = 20
    start = 140
    y = 642
    score_x = 156
    score_place = 55
    tk.Label(window, text=Card1[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card1[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card1_2_print(window, num):
    card12.score = Card1[num]['score']
    card12.bonus = Card1[num]['bonus']
    card12.green = Card1[num]['green']
    card12.gray = Card1[num]['gray']
    card12.blue = Card1[num]['blue']
    card12.black = Card1[num]['black']
    card12.red = Card1[num]['red']
    space = 20
    start = 308
    y = 642
    score_x = 325
    score_place = 55
    tk.Label(window, text=Card1[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card1[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

def Card1_3_print(window, num):
    card13.score = Card1[num]['score']
    card13.bonus = Card1[num]['bonus']
    card13.green = Card1[num]['green']
    card13.gray = Card1[num]['gray']
    card13.blue = Card1[num]['blue']
    card13.black = Card1[num]['black']
    card13.red = Card1[num]['red']
    space = 20
    start = 468
    y = 642
    score_x = 485
    score_place = 55
    tk.Label(window, text=Card1[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card1[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')


def Card1_4_print(window, num):
    card14.score = Card1[num]['score']
    card14.bonus = Card1[num]['bonus']
    card14.green = Card1[num]['green']
    card14.gray = Card1[num]['gray']
    card14.blue = Card1[num]['blue']
    card14.black = Card1[num]['black']
    card14.red = Card1[num]['red']
    space = 20
    start = 629
    y = 642
    score_x = 645
    score_place = 55
    tk.Label(window, text=Card1[num]['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x, y=y-41, anchor='nw')
    tk.Label(window, text='B', fg=trans(Card1[num]['bonus']), font=('PingHei', 16, "bold")).place(x=score_x+score_place, y=y-41,
                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,
                                                                                                               y=y,
                                                                                                               anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(Card1[num]['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

# print gems
def print_gumes(window):
    start = 186
    space = 87
    tk.Label(window, text=global_gems['green'], font=('PingHei', 15, "bold")).place(
        x=1357, y=start, anchor='nw')
    tk.Label(window, text=global_gems['gray'], font=('PingHei', 15, "bold")).place(
        x=1357, y=start + space, anchor='nw')
    tk.Label(window, text=global_gems['blue'], font=('PingHei', 15, "bold")).place(
        x=1357, y=start + space*2, anchor='nw')
    tk.Label(window, text=global_gems['black'], font=('PingHei', 15, "bold")).place(
        x=1357, y=start + space*3, anchor='nw')
    tk.Label(window, text=global_gems['red'], font=('PingHei', 15, "bold")).place(
        x=1357, y=start + space*4, anchor='nw')
    tk.Label(window, text=global_gems['gold'], font=('PingHei', 15, "bold")).place(
        x=1357, y=start + space*5, anchor='nw')

# print player
def print_player(window, num):
    score_x = 0
    if num == 0:
        score_x = 840
    if num == 1:
        score_x = 1005
    if num == 2:
        score_x = 1005 + 1005 - 840
    score_y = 603
    start = score_x - 26
    y = score_y+45
    space = 20
    tk.Label(window, text=player[num].score, font=('PingHei', 16, "bold")).place(x=score_x, y=score_y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].gems['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(x=start,y=y,anchor='nw')
    tk.Label(window, text=' ' + str(player[num].gems['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].gems['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].gems['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].gems['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].gems['gold']) + ' ', fg=gold_, font=('PingHei', 15, "bold")).place(
        x=start + space * 5, y=y, anchor='nw')
    y = y+19
    tk.Label(window, text=player[num].score, font=('PingHei', 16, "bold")).place(x=score_x, y=score_y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].bonus['green']) + ' ', fg=green_, font=('PingHei', 15, "bold")).place(
        x=start, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].bonus['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].bonus['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].bonus['black']) + ' ', fg=black_, font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].bonus['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].bonus['gold']) + ' ', fg=gold_, font=('PingHei', 15, "bold")).place(
        x=start + space * 5, y=y, anchor='nw')

    score_x = score_x + 5

    space = 20
    y = 493
    start = score_x - 16
    score_place = 55
    tk.Label(window, text=player[num].reserved1['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x,
                                                                                                          y=y - 41,
                                                                                                          anchor='nw')
    tk.Label(window, text='B', fg=trans(player[num].reserved1['bonus']), font=('PingHei', 16, "bold")).place(
        x=score_x + score_place, y=y - 41,
        anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved1['green']) + ' ', fg=green_,
             font=('PingHei', 15, "bold")).place(
        x=start,
        y=y,
        anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved1['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved1['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved1['black']) + ' ', fg=black_,
             font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved1['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

    space = 20
    y = 342
    start = score_x - 16
    score_place = 55
    tk.Label(window, text=player[num].reserved2['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x,
                                                                                                          y=y - 41,
                                                                                                          anchor='nw')
    tk.Label(window, text='B', fg=trans(player[num].reserved2['bonus']), font=('PingHei', 16, "bold")).place(
        x=score_x + score_place, y=y - 41,
        anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved2['green']) + ' ', fg=green_,
             font=('PingHei', 15, "bold")).place(
        x=start,
        y=y,
        anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved2['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved2['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved2['black']) + ' ', fg=black_,
             font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved2['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

    space = 20
    y = 186
    start = score_x - 16
    score_place = 55
    tk.Label(window, text=player[num].reserved3['score'], fg='black', font=('PingHei', 16, "bold")).place(x=score_x,
                                                                                                          y=y - 41,
                                                                                                          anchor='nw')
    tk.Label(window, text='B', fg=trans(player[num].reserved3['bonus']), font=('PingHei', 16, "bold")).place(
        x=score_x + score_place, y=y - 41,
        anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved3['green']) + ' ', fg=green_,
             font=('PingHei', 15, "bold")).place(
        x=start,
        y=y,
        anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved3['gray']) + ' ', fg=gray_, font=('PingHei', 15, "bold")).place(
        x=start + space, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved3['blue']) + ' ', fg=blue_, font=('PingHei', 15, "bold")).place(
        x=start + space * 2, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved3['black']) + ' ', fg=black_,
             font=('PingHei', 15, "bold")).place(
        x=start + space * 3, y=y, anchor='nw')
    tk.Label(window, text=' ' + str(player[num].reserved3['red']) + ' ', fg=red_, font=('PingHei', 15, "bold")).place(
        x=start + space * 4, y=y, anchor='nw')

# Apply for a noble
def Noble1_apply():
    if player[turn].bonus['green'] >= noble1.green and player[turn].bonus['gray'] >= noble1.gray and player[turn].bonus['blue'] >= noble1.blue and player[turn].bonus['black'] >= noble1.black and player[turn].bonus['red'] >= noble1.red :
        player[turn].score += noble1.score
        Noble1_print(window,10)
        print_player(window, turn)

def Noble2_apply():
    if player[turn].bonus['green'] >= noble2.green and player[turn].bonus['gray'] >= noble2.gray and player[turn].bonus['blue'] >= noble2.blue and player[turn].bonus['black'] >= noble2.black and player[turn].bonus['red'] >= noble2.red :
        player[turn].score += noble2.score
        Noble2_print(window,10)
        print_player(window, turn)

def Noble3_apply():
    if player[turn].bonus['green'] >= noble3.green and player[turn].bonus['gray'] >= noble3.gray and player[turn].bonus['blue'] >= noble3.blue and player[turn].bonus['black'] >= noble3.black and player[turn].bonus['red'] >= noble3.red :
        player[turn].score += noble3.score
        Noble3_print(window,10)
        print_player(window, turn)

def Noble4_apply():
    if player[turn].bonus['green'] >= noble4.green and player[turn].bonus['gray'] >= noble4.gray and player[turn].bonus['blue'] >= noble4.blue and player[turn].bonus['black'] >= noble4.black and player[turn].bonus['red'] >= noble4.red :
        player[turn].score += noble4.score
        Noble4_print(window,10)
        print_player(window, turn)

# Buy a card
def card_buy31():
    global Card3_top
    d = {}
    d["green"] = max(card31.green - player[turn].bonus['green'], 0)
    d["gray"] = max(card31.gray - player[turn].bonus['gray'], 0)
    d["blue"] = max(card31.blue - player[turn].bonus['blue'], 0)
    d["black"] = max(card31.black - player[turn].bonus['black'], 0)
    d["red"] = max(card31.red - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card31.bonus] += 1
    player[turn].score += card31.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card31.score = Card3[Card3_shuffle[Card3_top]]['score']
    card31.bonus = Card3[Card3_shuffle[Card3_top]]['bonus']
    card31.green = Card3[Card3_shuffle[Card3_top]]['green']
    card31.gray = Card3[Card3_shuffle[Card3_top]]['gray']
    card31.blue = Card3[Card3_shuffle[Card3_top]]['blue']
    card31.black = Card3[Card3_shuffle[Card3_top]]['black']
    card31.red = Card3[Card3_shuffle[Card3_top]]['red']
    print_gumes(window)
    print_player(window, turn)
    Card3_1_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_buy32():
    global Card3_top
    d = {}
    d["green"] = max(card32.green - player[turn].bonus['green'], 0)
    d["gray"] = max(card32.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card32.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card32.black - player[turn].bonus['black'],0)
    d["red"] = max(card32.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].score += card32.score
    player[turn].bonus[card32.bonus] += 1
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card32.score = Card3[Card3_shuffle[Card3_top]]['score']
    card32.bonus = Card3[Card3_shuffle[Card3_top]]['bonus']
    card32.green = Card3[Card3_shuffle[Card3_top]]['green']
    card32.gray = Card3[Card3_shuffle[Card3_top]]['gray']
    card32.blue = Card3[Card3_shuffle[Card3_top]]['blue']
    card32.black = Card3[Card3_shuffle[Card3_top]]['black']
    card32.red = Card3[Card3_shuffle[Card3_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card3_2_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_buy33():
    global Card3_top
    d = {}
    d["green"] = max(card33.green - player[turn].bonus['green'],0)
    d["gray"] = max(card33.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card33.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card33.black - player[turn].bonus['black'],0)
    d["red"] = max(card33.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card33.bonus] += 1
    player[turn].score += card33.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card33.score = Card3[Card3_shuffle[Card3_top]]['score']
    card33.bonus = Card3[Card3_shuffle[Card3_top]]['bonus']
    card33.green = Card3[Card3_shuffle[Card3_top]]['green']
    card33.gray = Card3[Card3_shuffle[Card3_top]]['gray']
    card33.blue = Card3[Card3_shuffle[Card3_top]]['blue']
    card33.black = Card3[Card3_shuffle[Card3_top]]['black']
    card33.red = Card3[Card3_shuffle[Card3_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card3_3_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_buy34():
    global Card3_top
    d = {}
    d["green"] = max(card34.green - player[turn].bonus['green'],0)
    d["gray"] = max(card34.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card34.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card34.black - player[turn].bonus['black'],0)
    d["red"] = max(card34.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card34.bonus] += 1
    player[turn].score += card34.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card34.score = Card3[Card3_shuffle[Card3_top]]['score']
    card34.bonus = Card3[Card3_shuffle[Card3_top]]['bonus']
    card34.green = Card3[Card3_shuffle[Card3_top]]['green']
    card34.gray = Card3[Card3_shuffle[Card3_top]]['gray']
    card34.blue = Card3[Card3_shuffle[Card3_top]]['blue']
    card34.black = Card3[Card3_shuffle[Card3_top]]['black']
    card34.red = Card3[Card3_shuffle[Card3_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card3_4_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_buy21():
    global Card2_top
    d = {}
    d["green"] = max(card21.green - player[turn].bonus['green'],0)
    d["gray"] = max(card21.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card21.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card21.black - player[turn].bonus['black'],0)
    d["red"] = max(card21.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card21.bonus] += 1
    player[turn].score += card21.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card21.score = Card2[Card2_shuffle[Card2_top]]['score']
    card21.bonus = Card2[Card2_shuffle[Card2_top]]['bonus']
    card21.green = Card2[Card2_shuffle[Card2_top]]['green']
    card21.gray = Card2[Card2_shuffle[Card2_top]]['gray']
    card21.blue = Card2[Card2_shuffle[Card2_top]]['blue']
    card21.black = Card2[Card2_shuffle[Card2_top]]['black']
    card21.red = Card2[Card2_shuffle[Card2_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card2_1_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_buy22():
    global Card2_top
    d = {}
    d["green"] = max(card22.green - player[turn].bonus['green'],0)
    d["gray"] = max(card22.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card22.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card22.black - player[turn].bonus['black'],0)
    d["red"] = max(card22.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card22.bonus] += 1
    player[turn].score += card22.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card22.score = Card2[Card2_shuffle[Card2_top]]['score']
    card22.bonus = Card2[Card2_shuffle[Card2_top]]['bonus']
    card22.green = Card2[Card2_shuffle[Card2_top]]['green']
    card22.gray = Card2[Card2_shuffle[Card2_top]]['gray']
    card22.blue = Card2[Card2_shuffle[Card2_top]]['blue']
    card22.black = Card2[Card2_shuffle[Card2_top]]['black']
    card22.red = Card2[Card2_shuffle[Card2_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card2_2_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_buy23():
    global Card2_top
    d = {}
    d["green"] = max(card23.green - player[turn].bonus['green'],0)
    d["gray"] = max(card23.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card23.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card23.black - player[turn].bonus['black'],0)
    d["red"] = max(card23.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card23.bonus] += 1
    player[turn].score += card23.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card23.score = Card2[Card2_shuffle[Card2_top]]['score']
    card23.bonus = Card2[Card2_shuffle[Card2_top]]['bonus']
    card23.green = Card2[Card2_shuffle[Card2_top]]['green']
    card23.gray = Card2[Card2_shuffle[Card2_top]]['gray']
    card23.blue = Card2[Card2_shuffle[Card2_top]]['blue']
    card23.black = Card2[Card2_shuffle[Card2_top]]['black']
    card23.red = Card2[Card2_shuffle[Card2_top]]['red']
    print_gumes(window)
    print_player(window, turn)
    Card2_3_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_buy24():
    global Card2_top
    d = {}
    d["green"] = max(card24.green - player[turn].bonus['green'],0)
    d["gray"] = max(card24.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card24.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card24.black - player[turn].bonus['black'],0)
    d["red"] = max(card24.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card24.bonus] += 1
    player[turn].score += card24.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card24.score = Card2[Card2_shuffle[Card2_top]]['score']
    card24.bonus = Card2[Card2_shuffle[Card2_top]]['bonus']
    card24.green = Card2[Card2_shuffle[Card2_top]]['green']
    card24.gray = Card2[Card2_shuffle[Card2_top]]['gray']
    card24.blue = Card2[Card2_shuffle[Card2_top]]['blue']
    card24.black = Card2[Card2_shuffle[Card2_top]]['black']
    card24.red = Card2[Card2_shuffle[Card2_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card2_4_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_buy11():
    global Card1_top
    d = {}

    d["green"] = max(card11.green - player[turn].bonus['green'],0)
    d["gray"] = max(card11.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card11.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card11.black - player[turn].bonus['black'],0)
    d["red"] = max(card11.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card11.bonus] += 1
    player[turn].score += card11.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card11.score = Card1[Card1_shuffle[Card1_top]]['score']
    card11.bonus = Card1[Card1_shuffle[Card1_top]]['bonus']
    card11.green = Card1[Card1_shuffle[Card1_top]]['green']
    card11.gray = Card1[Card1_shuffle[Card1_top]]['gray']
    card11.blue = Card1[Card1_shuffle[Card1_top]]['blue']
    card11.black = Card1[Card1_shuffle[Card1_top]]['black']
    card11.red = Card1[Card1_shuffle[Card1_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card1_1_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

def card_buy12():
    global Card1_top
    d = {}

    d["green"] = max(card12.green - player[turn].bonus['green'],0)
    d["gray"] = max(card12.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card12.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card12.black - player[turn].bonus['black'],0)
    d["red"] = max(card12.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card12.bonus] += 1
    player[turn].score += card12.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card12.score = Card1[Card1_shuffle[Card1_top]]['score']
    card12.bonus = Card1[Card1_shuffle[Card1_top]]['bonus']
    card12.green = Card1[Card1_shuffle[Card1_top]]['green']
    card12.gray = Card1[Card1_shuffle[Card1_top]]['gray']
    card12.blue = Card1[Card1_shuffle[Card1_top]]['blue']
    card12.black = Card1[Card1_shuffle[Card1_top]]['black']
    card12.red = Card1[Card1_shuffle[Card1_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card1_2_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

def card_buy13():
    global Card1_top
    d = {}

    d["green"] = max(card13.green - player[turn].bonus['green'],0)
    d["gray"] = max(card13.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card13.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card13.black - player[turn].bonus['black'],0)
    d["red"] = max(card13.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card13.bonus] += 1
    player[turn].score += card13.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card13.score = Card1[Card1_shuffle[Card1_top]]['score']
    card13.bonus = Card1[Card1_shuffle[Card1_top]]['bonus']
    card13.green = Card1[Card1_shuffle[Card1_top]]['green']
    card13.gray = Card1[Card1_shuffle[Card1_top]]['gray']
    card13.blue = Card1[Card1_shuffle[Card1_top]]['blue']
    card13.black = Card1[Card1_shuffle[Card1_top]]['black']
    card13.red = Card1[Card1_shuffle[Card1_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card1_3_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

def card_buy14():
    global Card1_top
    d = {}
    d["green"] = max(card14.green - player[turn].bonus['green'],0)
    d["gray"] = max(card14.gray - player[turn].bonus['gray'],0)
    d["blue"] = max(card14.blue - player[turn].bonus['blue'],0)
    d["black"] = max(card14.black - player[turn].bonus['black'],0)
    d["red"] = max(card14.red - player[turn].bonus['red'],0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum
    player[turn].bonus[card14.bonus] += 1
    player[turn].score += card14.score
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    card14.score = Card1[Card1_shuffle[Card1_top]]['score']
    card14.bonus = Card1[Card1_shuffle[Card1_top]]['bonus']
    card14.green = Card1[Card1_shuffle[Card1_top]]['green']
    card14.gray = Card1[Card1_shuffle[Card1_top]]['gray']
    card14.blue = Card1[Card1_shuffle[Card1_top]]['blue']
    card14.black = Card1[Card1_shuffle[Card1_top]]['black']
    card14.red = Card1[Card1_shuffle[Card1_top]]['red']

    print_gumes(window)
    print_player(window, turn)
    Card1_4_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

# reserve a card

def card_reserve30():
    global Card3_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = Card3[Card3_shuffle[Card3_top]]['score']
        player[turn].reserved1['bonus'] = Card3[Card3_shuffle[Card3_top]]['bonus']
        player[turn].reserved1['green'] = Card3[Card3_shuffle[Card3_top]]['green']
        player[turn].reserved1['gray'] = Card3[Card3_shuffle[Card3_top]]['gray']
        player[turn].reserved1['blue'] = Card3[Card3_shuffle[Card3_top]]['blue']
        player[turn].reserved1['black'] = Card3[Card3_shuffle[Card3_top]]['black']
        player[turn].reserved1['red'] = Card3[Card3_shuffle[Card3_top]]['red']
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = Card3[Card3_shuffle[Card3_top]]['score']
            player[turn].reserved2['bonus'] = Card3[Card3_shuffle[Card3_top]]['bonus']
            player[turn].reserved2['green'] = Card3[Card3_shuffle[Card3_top]]['green']
            player[turn].reserved2['gray'] = Card3[Card3_shuffle[Card3_top]]['gray']
            player[turn].reserved2['blue'] = Card3[Card3_shuffle[Card3_top]]['blue']
            player[turn].reserved2['black'] = Card3[Card3_shuffle[Card3_top]]['black']
            player[turn].reserved2['red'] = Card3[Card3_shuffle[Card3_top]]['red']
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = Card3[Card3_shuffle[Card3_top]]['score']
                player[turn].reserved3['bonus'] = Card3[Card3_shuffle[Card3_top]]['bonus']
                player[turn].reserved3['green'] = Card3[Card3_shuffle[Card3_top]]['green']
                player[turn].reserved3['gray'] = Card3[Card3_shuffle[Card3_top]]['gray']
                player[turn].reserved3['blue'] = Card3[Card3_shuffle[Card3_top]]['blue']
                player[turn].reserved3['black'] = Card3[Card3_shuffle[Card3_top]]['black']
                player[turn].reserved3['red'] = Card3[Card3_shuffle[Card3_top]]['red']
    print_player(window, turn)
    Card3_top += 1


def card_reserve31():
    global Card3_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card31.score
        player[turn].reserved1['bonus'] = card31.bonus
        player[turn].reserved1['green'] = card31.green
        player[turn].reserved1['gray'] = card31.gray
        player[turn].reserved1['blue'] = card31.blue
        player[turn].reserved1['black'] = card31.black
        player[turn].reserved1['red'] = card31.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card31.score
            player[turn].reserved2['bonus'] = card31.bonus
            player[turn].reserved2['green'] = card31.green
            player[turn].reserved2['gray'] = card31.gray
            player[turn].reserved2['blue'] = card31.blue
            player[turn].reserved2['black'] = card31.black
            player[turn].reserved2['red'] = card31.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card31.score
                player[turn].reserved3['bonus'] = card31.bonus
                player[turn].reserved3['green'] = card31.green
                player[turn].reserved3['gray'] = card31.gray
                player[turn].reserved3['blue'] = card31.blue
                player[turn].reserved3['black'] = card31.black
                player[turn].reserved3['red'] = card31.red
    print_player(window, turn)
    Card3_1_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_reserve32():
    global Card3_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card32.score
        player[turn].reserved1['bonus'] = card32.bonus
        player[turn].reserved1['green'] = card32.green
        player[turn].reserved1['gray'] = card32.gray
        player[turn].reserved1['blue'] = card32.blue
        player[turn].reserved1['black'] = card32.black
        player[turn].reserved1['red'] = card32.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card32.score
            player[turn].reserved2['bonus'] = card32.bonus
            player[turn].reserved2['green'] = card32.green
            player[turn].reserved2['gray'] = card32.gray
            player[turn].reserved2['blue'] = card32.blue
            player[turn].reserved2['black'] = card32.black
            player[turn].reserved2['red'] = card32.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card32.score
                player[turn].reserved3['bonus'] = card32.bonus
                player[turn].reserved3['green'] = card32.green
                player[turn].reserved3['gray'] = card32.gray
                player[turn].reserved3['blue'] = card32.blue
                player[turn].reserved3['black'] = card32.black
                player[turn].reserved3['red'] = card32.red
    print_player(window, turn)
    Card3_2_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_reserve33():
    global Card3_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card33.score
        player[turn].reserved1['bonus'] = card33.bonus
        player[turn].reserved1['green'] = card33.green
        player[turn].reserved1['gray'] = card33.gray
        player[turn].reserved1['blue'] = card33.blue
        player[turn].reserved1['black'] = card33.black
        player[turn].reserved1['red'] = card33.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card33.score
            player[turn].reserved2['bonus'] = card33.bonus
            player[turn].reserved2['green'] = card33.green
            player[turn].reserved2['gray'] = card33.gray
            player[turn].reserved2['blue'] = card33.blue
            player[turn].reserved2['black'] = card33.black
            player[turn].reserved2['red'] = card33.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card33.score
                player[turn].reserved3['bonus'] = card33.bonus
                player[turn].reserved3['green'] = card33.green
                player[turn].reserved3['gray'] = card33.gray
                player[turn].reserved3['blue'] = card33.blue
                player[turn].reserved3['black'] = card33.black
                player[turn].reserved3['red'] = card33.red
    print_player(window, turn)
    Card3_3_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_reserve34():
    global Card3_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card34.score
        player[turn].reserved1['bonus'] = card34.bonus
        player[turn].reserved1['green'] = card34.green
        player[turn].reserved1['gray'] = card34.gray
        player[turn].reserved1['blue'] = card34.blue
        player[turn].reserved1['black'] = card34.black
        player[turn].reserved1['red'] = card34.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card34.score
            player[turn].reserved2['bonus'] = card34.bonus
            player[turn].reserved2['green'] = card34.green
            player[turn].reserved2['gray'] = card34.gray
            player[turn].reserved2['blue'] = card34.blue
            player[turn].reserved2['black'] = card34.black
            player[turn].reserved2['red'] = card34.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card34.score
                player[turn].reserved3['bonus'] = card34.bonus
                player[turn].reserved3['green'] = card34.green
                player[turn].reserved3['gray'] = card34.gray
                player[turn].reserved3['blue'] = card34.blue
                player[turn].reserved3['black'] = card34.black
                player[turn].reserved3['red'] = card34.red
    print_player(window, turn)
    Card3_4_print(window, Card3_shuffle[Card3_top])
    Card3_top += 1

def card_reserve20():
    global Card2_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = Card2[Card2_shuffle[Card2_top]]['score']
        player[turn].reserved1['bonus'] = Card2[Card2_shuffle[Card2_top]]['bonus']
        player[turn].reserved1['green'] = Card2[Card2_shuffle[Card2_top]]['green']
        player[turn].reserved1['gray'] = Card2[Card2_shuffle[Card2_top]]['gray']
        player[turn].reserved1['blue'] = Card2[Card2_shuffle[Card2_top]]['blue']
        player[turn].reserved1['black'] = Card2[Card2_shuffle[Card2_top]]['black']
        player[turn].reserved1['red'] = Card2[Card2_shuffle[Card2_top]]['red']
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = Card2[Card2_shuffle[Card2_top]]['score']
            player[turn].reserved2['bonus'] = Card2[Card2_shuffle[Card2_top]]['bonus']
            player[turn].reserved2['green'] = Card2[Card2_shuffle[Card2_top]]['green']
            player[turn].reserved2['gray'] = Card2[Card2_shuffle[Card2_top]]['gray']
            player[turn].reserved2['blue'] = Card2[Card2_shuffle[Card2_top]]['blue']
            player[turn].reserved2['black'] = Card2[Card2_shuffle[Card2_top]]['black']
            player[turn].reserved2['red'] = Card2[Card2_shuffle[Card2_top]]['red']
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = Card2[Card2_shuffle[Card2_top]]['score']
                player[turn].reserved3['bonus'] = Card2[Card2_shuffle[Card2_top]]['bonus']
                player[turn].reserved3['green'] = Card2[Card2_shuffle[Card2_top]]['green']
                player[turn].reserved3['gray'] = Card2[Card2_shuffle[Card2_top]]['gray']
                player[turn].reserved3['blue'] = Card2[Card2_shuffle[Card2_top]]['blue']
                player[turn].reserved3['black'] = Card2[Card2_shuffle[Card2_top]]['black']
                player[turn].reserved3['red'] = Card2[Card2_shuffle[Card2_top]]['red']
    print_player(window, turn)
    Card2_top += 1

def card_reserve21():
    global Card2_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card21.score
        player[turn].reserved1['bonus'] = card21.bonus
        player[turn].reserved1['green'] = card21.green
        player[turn].reserved1['gray'] = card21.gray
        player[turn].reserved1['blue'] = card21.blue
        player[turn].reserved1['black'] = card21.black
        player[turn].reserved1['red'] = card21.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card21.score
            player[turn].reserved2['bonus'] = card21.bonus
            player[turn].reserved2['green'] = card21.green
            player[turn].reserved2['gray'] = card21.gray
            player[turn].reserved2['blue'] = card21.blue
            player[turn].reserved2['black'] = card21.black
            player[turn].reserved2['red'] = card21.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card21.score
                player[turn].reserved3['bonus'] = card21.bonus
                player[turn].reserved3['green'] = card21.green
                player[turn].reserved3['gray'] = card21.gray
                player[turn].reserved3['blue'] = card21.blue
                player[turn].reserved3['black'] = card21.black
                player[turn].reserved3['red'] = card21.red
    print_player(window, turn)
    Card2_1_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_reserve22():
    global Card2_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card22.score
        player[turn].reserved1['bonus'] = card22.bonus
        player[turn].reserved1['green'] = card22.green
        player[turn].reserved1['gray'] = card22.gray
        player[turn].reserved1['blue'] = card22.blue
        player[turn].reserved1['black'] = card22.black
        player[turn].reserved1['red'] = card22.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card22.score
            player[turn].reserved2['bonus'] = card22.bonus
            player[turn].reserved2['green'] = card22.green
            player[turn].reserved2['gray'] = card22.gray
            player[turn].reserved2['blue'] = card22.blue
            player[turn].reserved2['black'] = card22.black
            player[turn].reserved2['red'] = card22.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card22.score
                player[turn].reserved3['bonus'] = card22.bonus
                player[turn].reserved3['green'] = card22.green
                player[turn].reserved3['gray'] = card22.gray
                player[turn].reserved3['blue'] = card22.blue
                player[turn].reserved3['black'] = card22.black
                player[turn].reserved3['red'] = card22.red
    print_player(window, turn)
    Card2_2_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_reserve23():
    global Card2_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card23.score
        player[turn].reserved1['bonus'] = card23.bonus
        player[turn].reserved1['green'] = card23.green
        player[turn].reserved1['gray'] = card23.gray
        player[turn].reserved1['blue'] = card23.blue
        player[turn].reserved1['black'] = card23.black
        player[turn].reserved1['red'] = card23.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card23.score
            player[turn].reserved2['bonus'] = card23.bonus
            player[turn].reserved2['green'] = card23.green
            player[turn].reserved2['gray'] = card23.gray
            player[turn].reserved2['blue'] = card23.blue
            player[turn].reserved2['black'] = card23.black
            player[turn].reserved2['red'] = card23.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card23.score
                player[turn].reserved3['bonus'] = card23.bonus
                player[turn].reserved3['green'] = card23.green
                player[turn].reserved3['gray'] = card23.gray
                player[turn].reserved3['blue'] = card23.blue
                player[turn].reserved3['black'] = card23.black
                player[turn].reserved3['red'] = card23.red
    print_player(window, turn)
    Card2_3_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_reserve24():
    global Card2_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card24.score
        player[turn].reserved1['bonus'] = card24.bonus
        player[turn].reserved1['green'] = card24.green
        player[turn].reserved1['gray'] = card24.gray
        player[turn].reserved1['blue'] = card24.blue
        player[turn].reserved1['black'] = card24.black
        player[turn].reserved1['red'] = card24.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card24.score
            player[turn].reserved2['bonus'] = card24.bonus
            player[turn].reserved2['green'] = card24.green
            player[turn].reserved2['gray'] = card24.gray
            player[turn].reserved2['blue'] = card24.blue
            player[turn].reserved2['black'] = card24.black
            player[turn].reserved2['red'] = card24.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card24.score
                player[turn].reserved3['bonus'] = card24.bonus
                player[turn].reserved3['green'] = card24.green
                player[turn].reserved3['gray'] = card24.gray
                player[turn].reserved3['blue'] = card24.blue
                player[turn].reserved3['black'] = card24.black
                player[turn].reserved3['red'] = card24.red
    print_player(window, turn)
    Card2_4_print(window, Card2_shuffle[Card2_top])
    Card2_top += 1

def card_reserve10():
    global Card1_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = Card1[Card1_shuffle[Card1_top]]['score']
        player[turn].reserved1['bonus'] = Card1[Card1_shuffle[Card1_top]]['bonus']
        player[turn].reserved1['green'] = Card1[Card1_shuffle[Card1_top]]['green']
        player[turn].reserved1['gray'] = Card1[Card1_shuffle[Card1_top]]['gray']
        player[turn].reserved1['blue'] = Card1[Card1_shuffle[Card1_top]]['blue']
        player[turn].reserved1['black'] = Card1[Card1_shuffle[Card1_top]]['black']
        player[turn].reserved1['red'] = Card1[Card1_shuffle[Card1_top]]['red']
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = Card1[Card1_shuffle[Card1_top]]['score']
            player[turn].reserved2['bonus'] = Card1[Card1_shuffle[Card1_top]]['bonus']
            player[turn].reserved2['green'] = Card1[Card1_shuffle[Card1_top]]['green']
            player[turn].reserved2['gray'] = Card1[Card1_shuffle[Card1_top]]['gray']
            player[turn].reserved2['blue'] = Card1[Card1_shuffle[Card1_top]]['blue']
            player[turn].reserved2['black'] = Card1[Card1_shuffle[Card1_top]]['black']
            player[turn].reserved2['red'] = Card1[Card1_shuffle[Card1_top]]['red']
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = Card1[Card1_shuffle[Card1_top]]['score']
                player[turn].reserved3['bonus'] = Card1[Card1_shuffle[Card1_top]]['bonus']
                player[turn].reserved3['green'] = Card1[Card1_shuffle[Card1_top]]['green']
                player[turn].reserved3['gray'] = Card1[Card1_shuffle[Card1_top]]['gray']
                player[turn].reserved3['blue'] = Card1[Card1_shuffle[Card1_top]]['blue']
                player[turn].reserved3['black'] = Card1[Card1_shuffle[Card1_top]]['black']
                player[turn].reserved3['red'] = Card1[Card1_shuffle[Card1_top]]['red']
    print_player(window, turn)
    Card1_top += 1

def card_reserve11():
    global Card1_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card11.score
        player[turn].reserved1['bonus'] = card11.bonus
        player[turn].reserved1['green'] = card11.green
        player[turn].reserved1['gray'] = card11.gray
        player[turn].reserved1['blue'] = card11.blue
        player[turn].reserved1['black'] = card11.black
        player[turn].reserved1['red'] = card11.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card11.score
            player[turn].reserved2['bonus'] = card11.bonus
            player[turn].reserved2['green'] = card11.green
            player[turn].reserved2['gray'] = card11.gray
            player[turn].reserved2['blue'] = card11.blue
            player[turn].reserved2['black'] = card11.black
            player[turn].reserved2['red'] = card11.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card11.score
                player[turn].reserved3['bonus'] = card11.bonus
                player[turn].reserved3['green'] = card11.green
                player[turn].reserved3['gray'] = card11.gray
                player[turn].reserved3['blue'] = card11.blue
                player[turn].reserved3['black'] = card11.black
                player[turn].reserved3['red'] = card11.red
    print_player(window, turn)
    Card1_1_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

def card_reserve12():
    global Card1_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card12.score
        player[turn].reserved1['bonus'] = card12.bonus
        player[turn].reserved1['green'] = card12.green
        player[turn].reserved1['gray'] = card12.gray
        player[turn].reserved1['blue'] = card12.blue
        player[turn].reserved1['black'] = card12.black
        player[turn].reserved1['red'] = card12.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card12.score
            player[turn].reserved2['bonus'] = card12.bonus
            player[turn].reserved2['green'] = card12.green
            player[turn].reserved2['gray'] = card12.gray
            player[turn].reserved2['blue'] = card12.blue
            player[turn].reserved2['black'] = card12.black
            player[turn].reserved2['red'] = card12.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card12.score
                player[turn].reserved3['bonus'] = card12.bonus
                player[turn].reserved3['green'] = card12.green
                player[turn].reserved3['gray'] = card12.gray
                player[turn].reserved3['blue'] = card12.blue
                player[turn].reserved3['black'] = card12.black
                player[turn].reserved3['red'] = card12.red
    print_player(window, turn)
    Card1_2_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

def card_reserve13():
    global Card1_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card13.score
        player[turn].reserved1['bonus'] = card13.bonus
        player[turn].reserved1['green'] = card13.green
        player[turn].reserved1['gray'] = card13.gray
        player[turn].reserved1['blue'] = card13.blue
        player[turn].reserved1['black'] = card13.black
        player[turn].reserved1['red'] = card13.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card13.score
            player[turn].reserved2['bonus'] = card13.bonus
            player[turn].reserved2['green'] = card13.green
            player[turn].reserved2['gray'] = card13.gray
            player[turn].reserved2['blue'] = card13.blue
            player[turn].reserved2['black'] = card13.black
            player[turn].reserved2['red'] = card13.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card13.score
                player[turn].reserved3['bonus'] = card13.bonus
                player[turn].reserved3['green'] = card13.green
                player[turn].reserved3['gray'] = card13.gray
                player[turn].reserved3['blue'] = card13.blue
                player[turn].reserved3['black'] = card13.black
                player[turn].reserved3['red'] = card13.red
    print_player(window, turn)
    Card1_3_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

def card_reserve14():
    global Card1_top
    if player[turn].reserved1['occupied'] == 0:
        player[turn].reserved1['occupied'] = 1
        player[turn].reserved1['score'] = card14.score
        player[turn].reserved1['bonus'] = card14.bonus
        player[turn].reserved1['green'] = card14.green
        player[turn].reserved1['gray'] = card14.gray
        player[turn].reserved1['blue'] = card14.blue
        player[turn].reserved1['black'] = card14.black
        player[turn].reserved1['red'] = card14.red
    else:
        if player[turn].reserved2['occupied'] == 0:
            player[turn].reserved2['occupied'] = 1
            player[turn].reserved2['score'] = card14.score
            player[turn].reserved2['bonus'] = card14.bonus
            player[turn].reserved2['green'] = card14.green
            player[turn].reserved2['gray'] = card14.gray
            player[turn].reserved2['blue'] = card14.blue
            player[turn].reserved2['black'] = card14.black
            player[turn].reserved2['red'] = card14.red
        else:
            if player[turn].reserved3['occupied'] == 0:
                player[turn].reserved3['occupied'] = 1
                player[turn].reserved3['score'] = card14.score
                player[turn].reserved3['bonus'] = card14.bonus
                player[turn].reserved3['green'] = card14.green
                player[turn].reserved3['gray'] = card14.gray
                player[turn].reserved3['blue'] = card14.blue
                player[turn].reserved3['black'] = card14.black
                player[turn].reserved3['red'] = card14.red
    print_player(window, turn)
    Card1_4_print(window, Card1_shuffle[Card1_top])
    Card1_top += 1

# buy a reserved card
def reserved_card_buy01():
    d = {}
    d['green'] = max(player[turn].reserved1['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved1['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved1['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved1['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved1['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved1['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved1['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved1.keys():
        player[turn].reserved1[i] = 0
    print_player(window, turn)
    print_gumes(window)


def reserved_card_buy02():
    d = {}
    d['green'] = max(player[turn].reserved2['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved2['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved2['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved2['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved2['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved2['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved2['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved2.keys():
        player[turn].reserved2[i] = 0
    print_player(window, turn)
    print_gumes(window)


def reserved_card_buy03():
    d = {}
    d['green'] = max(player[turn].reserved3['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved3['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved3['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved3['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved3['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved3['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved3['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved3.keys():
        player[turn].reserved3[i] = 0
    print_player(window, turn)
    print_gumes(window)


def reserved_card_buy11():
    d = {}
    d['green'] = max(player[turn].reserved1['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved1['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved1['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved1['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved1['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved1['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved1['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved1.keys():
        player[turn].reserved1[i] = 0
    print_player(window, turn)
    print_gumes(window)


def reserved_card_buy12():
    d = {}
    d['green'] = max(player[turn].reserved2['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved2['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved2['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved2['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved2['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved2['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved2['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved2.keys():
        player[turn].reserved2[i] = 0
    print_player(window, turn)
    print_gumes(window)


def reserved_card_buy13():
    d = {}
    d['green'] = max(player[turn].reserved3['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved3['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved3['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved3['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved3['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved3['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved3['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved3.keys():
        player[turn].reserved3[i] = 0
    print_player(window, turn)
    print_gumes(window)

def reserved_card_buy21():
    d = {}
    d['green'] = max(player[turn].reserved1['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved1['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved1['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved1['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved1['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved1['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved1['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved1.keys():
        player[turn].reserved1[i] = 0
    print_player(window, turn)
    print_gumes(window)


def reserved_card_buy22():
    d = {}
    d['green'] = max(player[turn].reserved2['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved2['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved2['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved2['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved2['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved2['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved2['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved2.keys():
        player[turn].reserved2[i] = 0
    print_player(window, turn)
    print_gumes(window)


def reserved_card_buy23():
    d = {}
    d['green'] = max(player[turn].reserved3['green'] - player[turn].bonus['green'], 0)
    d['gray'] = max(player[turn].reserved3['gray'] - player[turn].bonus['gray'], 0)
    d['blue'] = max(player[turn].reserved3['blue'] - player[turn].bonus['blue'], 0)
    d['black'] = max(player[turn].reserved3['black'] - player[turn].bonus['black'], 0)
    d['red'] = max(player[turn].reserved3['red'] - player[turn].bonus['red'], 0)

    player[turn].gems['green'] -= d['green']
    player[turn].gems['gray'] -= d['gray']
    player[turn].gems['blue'] -= d['blue']
    player[turn].gems['black'] -= d['black']
    player[turn].gems['red'] -= d['red']
    goldnum = 0
    for i in d.keys():
        if player[turn].gems[i] < 0:
            d[i] = d[i] + player[turn].gems[i]
            goldnum = goldnum - player[turn].gems[i]
            player[turn].gems[i] = 0
    player[turn].gems['gold'] -= goldnum

    color = player[turn].reserved3['bonus']
    player[turn].bonus[color] += 1

    player[turn].score += player[turn].reserved3['score']
    global_gems['green'] += d['green']
    global_gems['gray'] += d['gray']
    global_gems['blue'] += d['blue']
    global_gems['black'] += d['black']
    global_gems['red'] += d['red']
    global_gems['gold'] += goldnum
    for i in player[turn].reserved3.keys():
        player[turn].reserved3[i] = 0
    print_player(window, turn)
    print_gumes(window)

# take gems

def take_gem_green():
    global turn
    global_gems['green'] -= 1
    player[turn].gems['green'] += 1
    print_player(window, turn)
    print_gumes(window)

def take_gem_gray():
    global turn
    global_gems['gray'] -= 1
    player[turn].gems['gray'] += 1
    print_player(window, turn)
    print_gumes(window)

def take_gem_blue():
    global turn
    global_gems['blue'] -= 1
    player[turn].gems['blue'] += 1
    print_player(window, turn)
    print_gumes(window)

def take_gem_black():
    global turn
    global_gems['black'] -= 1
    player[turn].gems['black'] += 1
    print_player(window, turn)
    print_gumes(window)

def take_gem_red():
    global turn
    global_gems['red'] -= 1
    player[turn].gems['red'] += 1
    print_player(window, turn)
    print_gumes(window)

def take_gem_gold():
    global turn
    global_gems['gold'] -= 1
    player[turn].gems['gold'] += 1
    print_player(window, turn)
    print_gumes(window)

# a player has finished
def OK():
    var[turn].set('                 ')
    change()
    var[turn].set('My Turn')

def buttons(window):
    Noble1_button = tk.Button(window, text="Apply", command=Noble1_apply)
    Noble1_button.place(x=170, y=240, anchor='nw')
    Noble2_button = tk.Button(window, text="Apply", command=Noble2_apply)
    Noble2_button.place(x=340, y=240, anchor='nw')
    Noble3_button = tk.Button(window, text="Apply", command=Noble3_apply)
    Noble3_button.place(x=500, y=240, anchor='nw')
    Noble4_button = tk.Button(window, text="Apply", command=Noble4_apply)
    Noble4_button.place(x=660, y=240, anchor='nw')

    card31_b = tk.Button(window, text="Buy", command=card_buy31)
    card31_b.place(x=135, y=390, anchor='nw')
    card31_r = tk.Button(window, text="Reserve", command=card_reserve31)
    card31_r.place(x=185, y=390, anchor='nw')
    card32_b = tk.Button(window, text="Buy", command=card_buy32)
    card32_b.place(x=305, y=390, anchor='nw')
    card32_r = tk.Button(window, text="Reserve", command=card_reserve32)
    card32_r.place(x=355, y=390, anchor='nw')
    card33_b = tk.Button(window, text="Buy", command=card_buy33)
    card33_b.place(x=465, y=390, anchor='nw')
    card33_r = tk.Button(window, text="Reserve", command=card_reserve33)
    card33_r.place(x=515, y=390, anchor='nw')
    card34_b = tk.Button(window, text="Buy", command=card_buy34)
    card34_b.place(x=625, y=390, anchor='nw')
    card34_r = tk.Button(window, text="Reserve", command=card_reserve34)
    card34_r.place(x=675, y=390, anchor='nw')
    card30_r = tk.Button(window, text="Reserve", command=card_reserve30)
    card30_r.place(x=20, y=390, anchor='nw')
    card21_b = tk.Button(window, text="Buy", command=card_buy21)
    card21_b.place(x=135, y=540, anchor='nw')
    card21_r = tk.Button(window, text="Reserve", command=card_reserve21)
    card21_r.place(x=185, y=540, anchor='nw')
    card22_b = tk.Button(window, text="Buy", command=card_buy22)
    card22_b.place(x=305, y=540, anchor='nw')
    card22_r = tk.Button(window, text="Reserve", command=card_reserve22)
    card22_r.place(x=355, y=540, anchor='nw')
    card23_b = tk.Button(window, text="Buy", command=card_buy23)
    card23_b.place(x=465, y=540, anchor='nw')
    card23_r = tk.Button(window, text="Reserve", command=card_reserve23)
    card23_r.place(x=515, y=540, anchor='nw')
    card24_b = tk.Button(window, text="Buy", command=card_buy24)
    card24_b.place(x=625, y=540, anchor='nw')
    card24_r = tk.Button(window, text="Reserve", command=card_reserve24)
    card24_r.place(x=675, y=540, anchor='nw')
    card20_r = tk.Button(window, text="Reserve", command=card_reserve20)
    card20_r.place(x=20, y=540, anchor='nw')
    card11_b = tk.Button(window, text="Buy", command=card_buy11)
    card11_b.place(x=135, y=690, anchor='nw')
    card11_r = tk.Button(window, text="Reserve", command=card_reserve11)
    card11_r.place(x=185, y=690, anchor='nw')
    card12_b = tk.Button(window, text="Buy", command=card_buy12)
    card12_b.place(x=305, y=690, anchor='nw')
    card12_r = tk.Button(window, text="Reserve", command=card_reserve12)
    card12_r.place(x=355, y=690, anchor='nw')
    card13_b = tk.Button(window, text="Buy", command=card_buy13)
    card13_b.place(x=465, y=690, anchor='nw')
    card13_r = tk.Button(window, text="Reserve", command=card_reserve13)
    card13_r.place(x=515, y=690, anchor='nw')
    card14_b = tk.Button(window, text="Buy", command=card_buy14)
    card14_b.place(x=625, y=690, anchor='nw')
    card14_r = tk.Button(window, text="Reserve", command=card_reserve14)
    card14_r.place(x=675, y=690, anchor='nw')
    card10_r = tk.Button(window, text="Reserve", command=card_reserve10)
    card10_r.place(x=20, y=690, anchor='nw')

    reserved01_b = tk.Button(window, text="Buy", command=reserved_card_buy01)
    reserved01_b.place(x=860, y=540, anchor='nw')
    reserved11_b = tk.Button(window, text="Buy", command=reserved_card_buy11)
    reserved11_b.place(x=1030, y=540, anchor='nw')
    reserved21_b = tk.Button(window, text="Buy", command=reserved_card_buy21)
    reserved21_b.place(x=1200, y=540, anchor='nw')
    reserved02_b = tk.Button(window, text="Buy", command=reserved_card_buy02)
    reserved02_b.place(x=860, y=390, anchor='nw')
    reserved12_b = tk.Button(window, text="Buy", command=reserved_card_buy12)
    reserved12_b.place(x=1030, y=390, anchor='nw')
    reserved22_b = tk.Button(window, text="Buy", command=reserved_card_buy22)
    reserved22_b.place(x=1200, y=390, anchor='nw')
    reserved03_b = tk.Button(window, text="Buy", command=reserved_card_buy03)
    reserved03_b.place(x=860, y=240, anchor='nw')
    reserved13_b = tk.Button(window, text="Buy", command=reserved_card_buy13)
    reserved13_b.place(x=1030, y=240, anchor='nw')
    reserved23_b = tk.Button(window, text="Buy", command=reserved_card_buy23)
    reserved23_b.place(x=1200, y=240, anchor='nw')

    space = 87
    green_gem = tk.Button(window, text="Take", command=take_gem_green)
    green_gem.place(x=1415, y=190, anchor='nw')
    gray_gem = tk.Button(window, text="Take", command=take_gem_gray)
    gray_gem.place(x=1415, y=190+space, anchor='nw')
    blue_gem = tk.Button(window, text="Take", command=take_gem_blue)
    blue_gem.place(x=1415, y=190+space*2, anchor='nw')
    black_gem = tk.Button(window, text="Take", command=take_gem_black)
    black_gem.place(x=1415, y=190+space*3, anchor='nw')
    red_gem = tk.Button(window, text="Take", command=take_gem_red)
    red_gem.place(x=1415, y=190+space*4, anchor='nw')
    gold_gem = tk.Button(window, text="Take", command=take_gem_gold)
    gold_gem.place(x=1415, y=190+space*5, anchor='nw')

    okbutton = tk.Button(window, text="OK", command=OK)
    okbutton.place(x=1370, y=695, anchor='nw')


def shuffle():
    random.shuffle(Noble_shuffle)
    random.shuffle(Card3_shuffle)
    random.shuffle(Card2_shuffle)
    random.shuffle(Card1_shuffle)

def init_print(window):
    global Card3_top
    global Card2_top
    global Card1_top

    buttons(window=window)

    Noble1_print(window=window, num=Noble_shuffle[0])
    Noble2_print(window=window, num=Noble_shuffle[1])
    Noble3_print(window=window, num=Noble_shuffle[2])
    Noble4_print(window=window, num=Noble_shuffle[3])

    Card3_1_print(window=window, num=Card3_shuffle[0])
    Card3_2_print(window=window, num=Card3_shuffle[1])
    Card3_3_print(window=window, num=Card3_shuffle[2])
    Card3_4_print(window=window, num=Card3_shuffle[3])
    Card3_top = 4

    Card2_1_print(window=window, num=Card2_shuffle[0])
    Card2_2_print(window=window, num=Card2_shuffle[1])
    Card2_3_print(window=window, num=Card2_shuffle[2])
    Card2_4_print(window=window, num=Card2_shuffle[3])
    Card2_top = 4

    Card1_1_print(window=window, num=Card1_shuffle[0])
    Card1_2_print(window=window, num=Card1_shuffle[1])
    Card1_3_print(window=window, num=Card1_shuffle[2])
    Card1_4_print(window=window, num=Card1_shuffle[3])
    Card1_top = 4

    print_gumes(window=window)

    print_player(window=window, num=0)
    print_player(window=window, num=1)
    print_player(window=window, num=2)

a = tk.StringVar()
b = tk.StringVar()
c = tk.StringVar()
var = [a, b, c]
var[0].set('')
var[1].set('')
var[2].set('')

def main():
    shuffle()
    window.title('Splendor - PinKU')
    window.geometry('1500x750')

    canvas = tk.Canvas(window, height=750, width=1500)
    image = tk.PhotoImage(file='UI.png')
    canvas.create_image(750, 0, anchor='n',image=image)
    canvas.pack()

    init_print(window=window)


    tk.Label(window, textvariable=var[0], fg='black', font=('Arial', 15) ).place(x=845, y=715, anchor='nw')
    tk.Label(window, textvariable=var[1], fg='black', font=('Arial', 15)).place(x=1010, y=715, anchor='nw')
    tk.Label(window, textvariable=var[2], fg='black', font=('Arial', 15)).place(x=1175, y=715, anchor='nw')


    var[turn].set('My Turn')



    window.mainloop()


if __name__ == '__main__':
    main()