# problem: https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html

size = input("How big should be your board: ")
b = 0

while b < int(size):
    a = 0
    while a < int(size):
        print(" ---", end="")
        a += 1

    print(" ")

    a = 0
    while a < int(size):
        print("|   ", end="")
        a += 1

    print("|")
    b += 1

a = 0
while a < int(size):
    print(" ---", end="")
    a += 1

print(" ")
