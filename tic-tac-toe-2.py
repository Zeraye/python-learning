import math
import random

board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

i = 0
numering = 0
while i < 3:
    k = 0
    while k < 3:
        board[i][k] = str(numering)
        numering += 1
        k += 1
    i += 1


def draw():
    i = 0
    while i < 3:
        print(board[i][0] + '|' + board[i][1] + '|' + board[i][2])
        i += 1


def choose():
    move = input("Give any free number (you're x) >> ")
    first = math.floor(int(move) / 3)
    second = int(move) % 3
    while board[first][second] == 'o':
        move = input("This field is already taken, give any free number (you're x) >> ")
        first = math.floor(int(move) / 3)
        second = int(move) % 3
    board[first][second] = 'x'


def check_win():
    return board[0][0] == board[0][1] == board[0][2] or \
           board[1][0] == board[1][1] == board[1][2] or \
           board[2][0] == board[2][1] == board[2][2] or \
           board[0][0] == board[1][0] == board[2][0] or \
           board[0][1] == board[1][1] == board[2][1] or \
           board[0][2] == board[1][2] == board[2][2] or \
           board[0][0] == board[1][1] == board[2][2] or \
           board[0][2] == board[1][1] == board[2][0]


def computer():
    first = random.randint(0, 2)
    second = random.randint(0, 2)
    while board[first][second] == 'x':
        first = random.randint(0, 2)
        second = random.randint(0, 2)
    board[first][second] = 'o'


while True:
    draw()
    choose()
    if check_win():
        draw()
        print("You have won!")
        break
    computer()
    if check_win():
        draw()
        print("You have lost.")
        break
