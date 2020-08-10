# problem: https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html

times = 0

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def draw():
    print(game[0][0], end=", ")
    print(game[0][1], end=", ")
    print(game[0][2], end="\n")
    print(game[1][0], end=", ")
    print(game[1][1], end=", ")
    print(game[1][2], end="\n")
    print(game[2][0], end=", ")
    print(game[2][1], end=", ")
    print(game[2][2], end="\n")


def player1():
    global times
    cor1 = input("[PLAYER 1] Where you want to put x? Type [row,col]: ")
    cor1_list = cor1.split(",")
    if game[int(cor1_list[0]) - 1][int(cor1_list[1]) - 1] == 0:
        game[int(cor1_list[0]) - 1][int(cor1_list[1]) - 1] = "x"
        times += 1
        draw()
    else:
        print("You can't put here x!")
        player1()


def player2():
    global times
    cor2 = input("[PLAYER 2] Where you want to put o? Type [row,col]: ")
    cor2_list = cor2.split(",")
    if game[int(cor2_list[0]) - 1][int(cor2_list[1]) - 1] == 0:
        game[int(cor2_list[0]) - 1][int(cor2_list[1]) - 1] = "o"
        times += 1
        draw()
    else:
        print("You can't put here o!")
        player2()


def check():
    global times
    i = 0
    while i < 3:
        if game[i][0] == "x" and game[i][1] == "x" and game[i][2] == "x":
            print("Player 1 WON!")
            times = 10
            break
        if game[i][0] == "o" and game[i][1] == "o" and game[i][2] == "o":
            print("Player 2 WON!")
            times = 10
            break
        i += 1

    i = 0
    while i < 3:
        if game[0][i] == "x" and game[1][i] == "x" and game[2][i] == "x":
            print("Player 1 WON!")
            times = 10
            break
        if game[0][i] == "o" and game[1][i] == "o" and game[2][i] == "o":
            print("Player 2 WON!")
            times = 10
            break
        i += 1
    if game[0][0] == "x" and game[1][1] == "x" and game[2][2] == "x"\
            or game[2][0] == "x" and game[1][1] == "x" and game[0][2] == "x":
        print("Player 1 WON!")
    if game[0][0] == "o" and game[1][1] == "o" and game[2][2] == "o"\
            or game[2][0] == "o" and game[1][1] == "o" and game[0][2] == "o":
        print("Player 2 WON!")
    if times == 9:
        print("DRAW!")


draw()
while times < 9:
    if times < 9:
        player1()
        check()
    if times < 9:
        player2()
        check()
