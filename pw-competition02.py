import random as r

good = 0
bad = 0

k = 0
while k < 1000000:
    mgla = []
    snieg = []
    i = 0
    while i < 7:
        a = r.randint(1, 6)
        if a == 1:
            mgla.append(1)
        else:
            pass

        b = r.randint(1, 3)
        if b == 1:
            snieg.append(1)
        else:
            pass

        i += 1

    if (len(mgla) == 0) and (len(snieg) <= 1):
        good += 1
    else:
        bad += 1

    k += 1
    if k % 1000 == 0:
        print(k)

print(good / (good + bad))
