# problem: https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

name_1 = input("First player name: ")
name_2 = input("Second player name: ")

i = 0
while i == 0:
    player_1 = input("[{}] Type rock, paper, or scissors: ".format(name_1))
    if player_1 == "rock" or player_1 == "paper" or player_1 == "scissors":
        i = 1
else:
    pass

i = 0
while i == 0:
    player_2 = input("[{}] Type rock, paper, or scissors: ".format(name_2))
    if player_2 == "rock" or player_2 == "paper" or player_2 == "scissors":
        i = 1
else:
    pass

if player_1 == player_2:
    print("Draw!")
elif (player_1 == "rock" and player_2 == "scissors") or\
        (player_1 == "paper" and player_2 == "rock") or\
        (player_1 == "scissors" and player_2 == "paper"):
    print("{} won!".format(name_1))
else:
    print("{} won!".format(name_2))
