import random as r

good = 0
total = 0
k = 0

while k < 1000000:
    k = k + 1
    i = 0
    white = 0
    other = 0

    while i < 3:
        i = i + 1
        x = r.randint(1, 8)

        if 1 <= x <= 4:
            white = white + 1
        if 5 <= x <= 8:
            other = other + 1

    i = 0

    if white == 0:
        pass
    if white == 1:
        y1 = r.randint(1, 6)
        if y1 == 4:
            good = good + 1
    if white == 2:
        y1 = r.randint(1, 6)
        y2 = r.randint(1, 6)
        if y1 == 4 or y2 == 4:
            good = good + 1
    if white == 3:
        y1 = r.randint(1, 6)
        y2 = r.randint(1, 6)
        y3 = r.randint(1, 6)
        if y1 == 4 or y2 == 4 or y3 == 4:
            good = good + 1

    total = total + 1
    print(good / total)
