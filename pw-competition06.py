import random as r

t = 0
gry = 0
pozytywne = 0
while t < 1000000:
    i = 0
    p = 0
    suma = 0
    while p < 3:
        suma += r.randint(1, 4)
        p += 1
    if suma < 6:
        gry += 1
        pozytywne += 1
    else:
        gry += 1
    t += 1
    print((gry*100)/1000000, ' %')

print(pozytywne/gry)
