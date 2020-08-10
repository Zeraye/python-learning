# Program jeszcze nie skończony
import random as r
import sys

arr = ["?", "?", "?", "?", "?", "?", "?", "?", "?"]
a = [0, 3, 6]
b = [1, 4, 7]
c = [2, 5, 8]
end = 0


def draw():
    print("  |", "A", "|", "B", "|", "C", "|")
    print("1 |", arr[0], "|", arr[1], "|", arr[2], "|")
    print("2 |", arr[3], "|", arr[4], "|", arr[5], "|")
    print("3 |", arr[6], "|", arr[7], "|", arr[8], "|")


def play(p):
    while True:
        move = input("Wpisz numer pola (np. A2) >> ")
        if int(move[1]) < 0 or int(move[1]) > 2:
            print("Błąd!")
            sys.exit()
        if move[0] == "A" or move[0] == "a":
            pos = a[int(move[1]) - 1]
        elif move[0] == "B" or move[0] == "b":
            pos = b[int(move[1]) - 1]
        elif move[0] == "C" or move[0] == "c":
            pos = c[int(move[1]) - 1]
        else:
            print("Błąd!")
            sys.exit()
        if arr[pos] == "?":
            arr[pos] = p
            break
        else:
            print("Złe pole, wybierz jeszcze raz!")


def check(p):
    global end
    if arr[0] == arr[1] == arr[2] != "?" or arr[3] == arr[4] == arr[5] != "?" or arr[6] == arr[7] == arr[8] != "?" or \
            arr[0] == arr[3] == arr[6] != "?" or arr[1] == arr[4] == arr[7] != "?" or arr[2] == arr[5] == arr[
        8] != "?" or arr[0] == arr[4] == arr[8] != "?" or arr[2] == arr[4] == arr[6] != "?":
        print("Wygrał ", p)
        end = 1
    else:
        pass


mode = input("Chcesz zagrać z komputerem czy 2 osobą (k/o) >> ")
if mode != "k" and mode != "o":
    print("Błąd!")
    sys.exit()

if mode == "o":
    draw()
    print("Zaczyna O")
    while True:
        play("O")
        draw()
        check("O")
        if end == 1:
            break
        play("X")
        draw()
        check("X")
        if end == 1:
            break

if mode == "k":
    first = input("Czy chcesz zaczynać (t/n) >> ")
    draw()
    if first == "t":
        while True:
            play("O")
            check("O")
            if end == 1:
                break
            while True:
                random = r.randint(0, 8)
                if arr[random] != "?":
                    pass
                else:
                    break
            arr[random] = "X"
            draw()
            check("X")
            if end == 1:
                break
