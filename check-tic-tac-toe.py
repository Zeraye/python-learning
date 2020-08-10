# problem: https://www.practicepython.org/exercise/2015/11/16/26-check-tic-tac-toe.html

game1 = [[1, 2, 0],
         [2, 1, 0],
         [2, 1, 1]]

game2 = [[2, 2, 0],
         [2, 1, 0],
         [2, 1, 1]]

game3 = [[1, 2, 0],
         [2, 1, 0],
         [2, 1, 1]]

game4 = [[0, 1, 0],
         [2, 1, 0],
         [2, 1, 1]]

game5 = [[1, 2, 0],
         [2, 1, 0],
         [2, 1, 2]]

game6 = [[1, 2, 0],
         [2, 1, 0],
         [2, 1, 0]]

game = game1
win = 0
i = 0
while i < 3:
    if game[i][0] == 1 and game[i][1] == 1 and game[i][2] == 1:
        print("FIRST PLAYER WON [ROW]")
        win = 1
        break
    if game[i][0] == 2 and game[i][1] == 2 and game[i][2] == 2:
        print("SECOND PLAYER WON [ROW]")
        win = 1
        break
    i += 1

i = 0
while i < 3:
    if game[i][0] == 1 and game[i][0] == 1 and game[i][0] == 1\
            or game[i][1] == 1 and game[i][1] == 1 and game[i][1] == 1\
            or game[i][2] == 1 and game[i][2] == 1 and game[i][2] == 1:
        print("FIRST PLAYER WON [COLUMN]")
        win = 1
        break
    if game[i][0] == 2 and game[i][0] == 2 and game[i][0] == 2\
            or game[i][1] == 2 and game[i][1] == 2 and game[i][1] == 2\
            or game[i][2] == 2 and game[i][2] == 2 and game[i][2] == 2:
        print("SECOND PLAYER WON [COLUMN]")
        win = 1
        break
    i += 1

if not win:
    print("DRAW")
