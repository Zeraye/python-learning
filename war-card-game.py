import random as r
import time
cards = [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]  # 11-J, 12-Q, 13-K, 14-A
color = [1, 2, 3, 4]  # 1-wino, 2-serce, 3-żołądź, 4-kryształek
deck = []

player = []
computer = []
waiting = []

i = 0
k = 0
while k < 3:
    i = 0
    while i < 12:
        deck.append([cards[i], color[k]])
        i += 1
    k += 1

i = 0
while i < 26:
    player.append(deck[r.randint(0, len(deck) - 1)])
    i += 1
i = 0
while i < 26:
    computer.append(deck[r.randint(0, len(deck) - 1)])
    i += 1


def check_win():
    if len(computer) == 0:
        out_of_cards = "Computer"
    else:
        out_of_cards = "Player"
    if len(computer) + len(player) != 52 and (len(computer) == 0 or len(player) == 0):
        print("Game ended while draw! {} is out of cards!".format(out_of_cards))
    if len(computer) == 0:
        print("Player has won!")
        quit()
    elif len(player) == 0:
        print("Computer has won!")
        quit()


print("Let's start!")
print("\n")
num_of_games = 0
result = "default (error)"
while len(player) != 0 or len(computer) != 0:
    num_of_games += 1
    # time.sleep(1)
    check_win()
    num_player = r.randint(0, len(player) - 1)
    num_computer = r.randint(0, len(computer) - 1)
    if player[num_player][0] > computer[num_computer][0]:
        player.append(computer[num_computer])
        computer.pop(num_computer)
        result = "win"
    elif player[num_player][0] < computer[num_computer][0]:
        computer.append(player[num_player])
        player.pop(num_player)
        result = "lost"
    elif player[num_player][0] == computer[num_computer][0]:
        while player[num_player][0] == computer[num_computer][0]:
            waiting.append(player[num_player])
            player.pop(num_player)
            waiting.append(computer[num_computer])
            computer.pop(num_computer)
            check_win()
            num_player = r.randint(0, len(player) - 1)
            num_computer = r.randint(0, len(computer) - 1)
            waiting.append(player[num_player])
            player.pop(num_player)
            waiting.append(computer[num_computer])
            computer.pop(num_computer)
            check_win()
            num_player = r.randint(0, len(player) - 1)
            num_computer = r.randint(0, len(computer) - 1)
        if player[num_player][0] > computer[num_computer][0]:
            i = 0
            while i < len(waiting):
                player.append(waiting[i])
                i += 1
            result = "win"
        elif player[num_player][0] < computer[num_computer][0]:
            i = 0
            while i < len(waiting):
                computer.append(waiting[i])
                i += 1
            result = "lost"
        waiting = []
    print("You {} this turn!".format(result))
    print("My cards: {}".format(len(player)))
    print("Computer cards: {}".format(len(computer)))
    print("Game: {}".format(num_of_games))
    print("\n")
