# problem: https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
import random

rand = str(random.randint(1, 9))
i = 0
tries = 0

while i == 0:
    num = input("Type digit from 1 to 9: ")
    if num == "exit":
        exit()
    else:
        if num == rand:
            tries += 1
            print("Correct! Tries: {}".format(tries))
            i = 1
        elif num < rand:
            tries += 1
            print("Higher!")
        elif num > rand:
            tries += 1
            print("Lower!")
