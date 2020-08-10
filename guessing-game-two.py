# problem: https://www.practicepython.org/exercise/2015/11/01/25-guessing-game-two.html
import math


def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier + 0.5) / multiplier


print("Think about a number between 0 and 100.")
number = 50
step = 2

run = True
while run:
    attempt = input("Did you think about {}? Write [too low, too high or yes]: ".format(int(number)))
    step *= 2

    if attempt == "too low":
        number += round_half_up(100 / step)
    elif attempt == "too high":
        number -= round_half_up(100 / step)
    elif attempt == "yes":
        print("Thanks for game!")
        run = False
    else:
        run = False
