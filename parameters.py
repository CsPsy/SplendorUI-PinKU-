# parameters - classes and parameters

import tkinter as tk

class Player:
    def __init__(self):
        self.score = 0
        self.gems = {'green':0, 'gray':0,'blue':0,'black':0,'red':0, 'gold':0}
        self.bonus = {'green':0, 'gray':0,'blue':0,'black':0,'red':0, 'gold':0}
        self.reserved1 = {'occupied':0, 'score': 0, 'bonus':0, 'green': 0, 'gray': 0, 'blue':0, 'black': 0, 'red': 0}
        self.reserved2 = {'occupied':0, 'score': 0, 'bonus':0, 'green': 0, 'gray': 0, 'blue': 0, 'black': 0, 'red': 0}
        self.reserved3 = {'occupied':0, 'score': 0, 'bonus':0, 'green': 0, 'gray': 0, 'blue': 0, 'black': 0, 'red': 0}

class card:
    def __init__(self):
        self.score = 0
        self.bonus = 0
        self.green = 0
        self.gray = 0
        self.blue = 0
        self.black = 0
        self.red = 0

class noble:
    def __init__(self):
        self.score = 3
        self.green = 0
        self.gray = 0
        self.blue = 0
        self.black = 0
        self.red = 0


# 3 players
a = Player()
b = Player()
c = Player()
player = [a, b, c]

# 4 nobles
noble1 = noble()
noble2 = noble()
noble3 = noble()
noble4 = noble()


# 4 level3 cards
card31 = card()
card32 = card()
card33 = card()
card34 = card()

# 4 level2 cards
card21 = card()
card22 = card()
card23 = card()
card24 = card()

# 4 level1 cards
card11 = card()
card12 = card()
card13 = card()
card14 = card()


# 10 Nobles one for 3 points
Noble = [
    {'green': 4, 'gray': 0, 'blue':0, 'black': 0, 'red': 4},
    {'green': 0, 'gray': 4, 'blue':4, 'black': 0, 'red': 0},
    {'green': 0, 'gray': 0, 'blue':0, 'black': 4, 'red': 4},
    {'green': 0, 'gray': 4, 'blue':0, 'black': 4, 'red': 0},
    {'green': 4, 'gray': 0, 'blue':4, 'black': 0, 'red': 0},
    {'green': 3, 'gray': 0, 'blue':0, 'black': 3, 'red': 3},
    {'green': 0, 'gray': 3, 'blue':3, 'black': 3, 'red': 0},
    {'green': 3, 'gray': 3, 'blue':3, 'black': 0, 'red': 0},
    {'green': 3, 'gray': 0, 'blue':3, 'black': 0, 'red': 3},
    {'green': 0, 'gray': 3, 'blue':0, 'black': 3, 'red': 3},
    {'green': 0, 'gray': 0, 'blue':0, 'black': 0, 'red': 0},
]

# 20 level 3 cards
Card3 = [
    {'score': 5, 'bonus': 'black', 'green': 0, 'gray': 0, 'blue': 0, 'black': 3, 'red': 7},
    {'score': 5, 'bonus': 'red', 'green': 7, 'gray': 0, 'blue': 0, 'black': 0, 'red': 3},
    {'score': 3, 'bonus': 'red', 'green': 3, 'gray': 3, 'blue': 5, 'black': 3, 'red': 0},
    {'score': 4, 'bonus': 'black', 'green': 0, 'gray': 0, 'blue': 0, 'black': 0, 'red': 7},
    {'score': 4, 'bonus': 'green', 'green': 3, 'gray': 3, 'blue': 6, 'black': 0, 'red': 0},
    {'score': 4, 'bonus': 'green', 'green': 0, 'gray': 0, 'blue': 7, 'black': 0, 'red': 0},
    {'score': 5, 'bonus': 'green', 'green': 3, 'gray': 0, 'blue': 7, 'black': 0, 'red': 0},
    {'score': 3, 'bonus': 'green', 'green': 0, 'gray': 5, 'blue': 3, 'black': 3, 'red': 3},
    {'score': 3, 'bonus': 'black', 'green': 5, 'gray': 3, 'blue': 3, 'black': 0, 'red': 3},
    {'score': 4, 'bonus': 'red', 'green': 7, 'gray': 0, 'blue': 0, 'black': 0, 'red': 0},
    {'score': 3, 'bonus': 'gray', 'green': 3, 'gray': 0, 'blue': 3, 'black': 3, 'red': 5},
    {'score': 5, 'bonus': 'blue', 'green': 0, 'gray': 7, 'blue': 3, 'black': 0, 'red': 0},
    {'score': 4, 'bonus': 'gray', 'green': 0, 'gray': 0, 'blue': 0, 'black': 7, 'red': 0},
    {'score': 4, 'bonus': 'red', 'green': 6, 'gray': 0, 'blue': 3, 'black': 0, 'red': 3},
    {'score': 4, 'bonus': 'blue', 'green': 0, 'gray': 6, 'blue': 3, 'black': 3, 'red': 0},
    {'score': 4, 'bonus': 'black', 'green': 3, 'gray': 0, 'blue': 0, 'black': 3, 'red': 6},
    {'score': 4, 'bonus': 'blue', 'green': 0, 'gray': 7, 'blue': 0, 'black': 0, 'red': 0},
    {'score': 3, 'bonus': 'blue', 'green': 3, 'gray': 3, 'blue': 3, 'black': 5, 'red': 3},
    {'score': 4, 'bonus': 'gray', 'green': 0, 'gray': 3, 'blue': 0, 'black': 6, 'red': 3},
    {'score': 5, 'bonus': 'gray', 'green': 0, 'gray': 3, 'blue': 0, 'black': 7, 'red': 0},

]

# 30 level 2 cards
Card2 = [
         {'score': 1, 'bonus':'green', 'green': 0, 'gray': 2, 'blue': 3, 'black': 2, 'red': 0},
         {'score': 2, 'bonus':'blue', 'green': 0, 'gray': 0, 'blue': 5, 'black': 0, 'red': 0},
         {'score': 1, 'bonus':'gray', 'green': 0, 'gray': 2, 'blue': 3, 'black': 0, 'red': 3},
         {'score': 2, 'bonus':'red', 'green': 0, 'gray': 0, 'blue': 0, 'black': 5, 'red': 0},
         {'score': 3, 'bonus':'gray', 'green': 0, 'gray': 6, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 3, 'bonus':'red', 'green': 0, 'gray': 0, 'blue': 0, 'black': 0, 'red': 6},
         {'score': 2, 'bonus':'green', 'green': 0, 'gray': 4, 'blue': 2, 'black': 1, 'red': 0},
         {'score': 1, 'bonus':'gray', 'green': 3, 'gray': 0, 'blue': 0, 'black': 2, 'red': 2},
         {'score': 2, 'bonus':'gray', 'green': 1, 'gray': 0, 'blue': 0, 'black': 2, 'red': 4},
         {'score': 2, 'bonus':'green', 'green': 5, 'gray': 0, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 1, 'bonus':'blue', 'green': 2, 'gray': 0, 'blue': 2, 'black': 0, 'red': 3},
         {'score': 1, 'bonus':'blue', 'green': 3, 'gray': 0, 'blue': 2, 'black': 3, 'red': 0},
         {'score': 2, 'bonus':'black', 'green': 0, 'gray': 5, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 1, 'bonus':'green', 'green': 2, 'gray': 3, 'blue': 0, 'black': 0, 'red': 3},
         {'score': 1, 'bonus':'red', 'green': 0, 'gray': 2, 'blue': 0, 'black': 3, 'red': 2},
         {'score': 2, 'bonus':'red', 'green': 2, 'gray': 1, 'blue': 4, 'black': 0, 'red': 0},
         {'score': 1, 'bonus':'black', 'green': 3, 'gray': 3, 'blue': 0, 'black': 2, 'red': 0},
         {'score': 2, 'bonus':'green', 'green': 3, 'gray': 0, 'blue': 5, 'black': 0, 'red': 0},
         {'score': 2, 'bonus':'blue', 'green': 0, 'gray': 5, 'blue': 3, 'black': 0, 'red': 0},
         {'score': 2, 'bonus':'gray', 'green': 0, 'gray': 0, 'blue': 0, 'black': 3, 'red': 5},
         {'score': 3, 'bonus':'green', 'green': 6, 'gray': 0, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 3, 'bonus':'black', 'green': 0, 'gray': 0, 'blue': 0, 'black': 6, 'red': 0},
         {'score': 2, 'bonus':'black', 'green': 5, 'gray': 0, 'blue': 0, 'black': 0, 'red': 3},
         {'score': 1, 'bonus':'black', 'green': 2, 'gray': 3, 'blue': 2, 'black': 0, 'red': 0},
         {'score': 1, 'bonus':'red', 'green': 0, 'gray': 0, 'blue': 3, 'black': 3, 'red': 2},
         {'score': 3, 'bonus':'blue', 'green': 0, 'gray': 0, 'blue': 6, 'black': 0, 'red': 0},
         {'score': 2, 'bonus':'blue', 'green': 0, 'gray': 2, 'blue': 0, 'black': 4, 'red': 1},
         {'score': 2, 'bonus':'red', 'green': 0, 'gray': 3, 'blue': 0, 'black': 5, 'red': 0},
         {'score': 2, 'bonus':'black', 'green': 4, 'gray': 0, 'blue': 1, 'black': 0, 'red': 2},
         {'score': 2, 'bonus':'gray', 'green': 0, 'gray': 0, 'blue': 0, 'black': 0, 'red': 5},
]

# 40 level1 cards
Card1 = [
         {'score': 0, 'bonus': 'blue', 'green': 3, 'gray': 0, 'blue': 1, 'black': 0, 'red': 1},
         {'score': 0, 'bonus': 'blue', 'green': 0, 'gray': 0, 'blue': 0, 'black': 3, 'red': 0},
         {'score': 0, 'bonus': 'blue', 'green': 0, 'gray': 1, 'blue': 0, 'black': 2, 'red': 0},
         {'score': 0, 'bonus': 'red', 'green': 0, 'gray': 1, 'blue': 0, 'black': 3, 'red': 1},
         {'score': 0, 'bonus': 'red', 'green': 1, 'gray': 2, 'blue': 1, 'black': 1, 'red': 0},
         {'score': 0, 'bonus': 'red', 'green': 1, 'gray': 2, 'blue': 0, 'black': 2, 'red': 0},
         {'score': 0, 'bonus': 'black', 'green': 1, 'gray': 1, 'blue': 1, 'black': 0, 'red': 1},
         {'score': 0, 'bonus': 'black', 'green': 1, 'gray': 0, 'blue': 0, 'black': 1, 'red': 3},
         {'score': 0, 'bonus': 'black', 'green': 1, 'gray': 1, 'blue': 2, 'black': 0, 'red': 1},
         {'score': 0, 'bonus': 'black', 'green': 3, 'gray': 0, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'black', 'green': 2, 'gray': 0, 'blue': 0, 'black': 0, 'red': 1},
         {'score': 1, 'bonus': 'green', 'green': 0, 'gray': 0, 'blue': 0, 'black': 4, 'red': 0},
         {'score': 0, 'bonus': 'green', 'green': 0, 'gray': 0, 'blue': 0, 'black': 0, 'red': 3},
         {'score': 0, 'bonus': 'green', 'green': 0, 'gray': 0, 'blue': 2, 'black': 0, 'red': 2},
         {'score': 0, 'bonus': 'green', 'green': 0, 'gray': 1, 'blue': 1, 'black': 1, 'red': 1},
         {'score': 0, 'bonus': 'green', 'green': 0, 'gray': 1, 'blue': 1, 'black': 1, 'red': 1},
         {'score': 0, 'bonus': 'green', 'green': 0, 'gray': 1, 'blue': 1, 'black': 2, 'red': 1},
         {'score': 0, 'bonus': 'green', 'green': 0, 'gray': 0, 'blue': 1, 'black': 2, 'red': 2},
         {'score': 0, 'bonus': 'red', 'green': 1, 'gray': 1, 'blue': 1, 'black': 1, 'red': 0},
         {'score': 0, 'bonus': 'red', 'green': 0, 'gray': 2, 'blue': 0, 'black': 0, 'red': 2},
         {'score': 0, 'bonus': 'gray', 'green': 2, 'gray': 0, 'blue': 1, 'black': 1, 'red': 1},
         {'score': 0, 'bonus': 'gray', 'green': 2, 'gray': 0, 'blue': 2, 'black': 1, 'red': 0},
         {'score': 0, 'bonus': 'blue', 'green': 2, 'gray': 1, 'blue': 0, 'black': 0, 'red': 2},
         {'score': 0, 'bonus': 'gray', 'green': 0, 'gray': 0, 'blue': 3, 'black': 0, 'red': 0},
         {'score': 1, 'bonus': 'gray', 'green': 4, 'gray': 0, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'green', 'green': 1, 'gray': 1, 'blue': 3, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'green', 'green': 0, 'gray': 2, 'blue': 1, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'red', 'green': 0, 'gray': 3, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'red', 'green': 1, 'gray': 0, 'blue': 2, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'gray', 'green': 0, 'gray': 0, 'blue': 0, 'black': 1, 'red': 2},
         {'score': 0, 'bonus': 'gray', 'green': 0, 'gray': 0, 'blue': 2, 'black': 2, 'red': 0},
         {'score': 0, 'bonus': 'gray', 'green': 0, 'gray': 3, 'blue': 1, 'black': 1, 'red': 0},
         {'score': 0, 'bonus': 'gray', 'green': 1, 'gray': 0, 'blue': 1, 'black': 1, 'red': 1},
         {'score': 1, 'bonus': 'blue', 'green': 0, 'gray': 0, 'blue': 0, 'black': 0, 'red': 4},
         {'score': 0, 'bonus': 'blue', 'green': 2, 'gray': 0, 'blue': 0, 'black': 2, 'red': 0},
         {'score': 0, 'bonus': 'blue', 'green': 1, 'gray': 1, 'blue': 0, 'black': 1, 'red': 1},
         {'score': 0, 'bonus': 'blue', 'green': 1, 'gray': 1, 'blue': 0, 'black': 1, 'red': 2},
         {'score': 1, 'bonus': 'black', 'green': 0, 'gray': 0, 'blue': 4, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'black', 'green': 2, 'gray': 2, 'blue': 0, 'black': 0, 'red': 0},
         {'score': 0, 'bonus': 'black', 'green': 0, 'gray': 2, 'blue': 2, 'black': 0, 'red': 1},
         {'score': 1, 'bonus': 'red', 'green': 0, 'gray': 4, 'blue': 0, 'black': 0, 'red': 0},
]


# gems
global_gems = {'green': 5, 'gray': 5, 'blue': 5, 'black': 5, 'red': 5, 'gold': 5}

# colors
green_ = '#7ccbb4'
gray_ ='#bab7b0'
blue_ = '#6fb5cb'
black_ = '#33322d'
red_ = '#fe7453'
gold_ = '#f1bf52'

# shuffle cards
Noble_shuffle = [i for i in range(10)]
Card3_top = 0
Card3_shuffle = [i for i in range(20)]
Card2_top = 0
Card2_shuffle = [i for i in range(30)]
Card1_top = 0
Card1_shuffle = [i for i in range(40)]

# window
window = tk.Tk()

# who's turn
turn = 0