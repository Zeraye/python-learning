import random as r

f = open('plemiona-poparcie.txt', 'w')
arr = []

t = 0
h = 10000000
k = 0
while t < h:
    t += 1
    p = 0
    suma = 0
    while p < 4:
        p += 1
        suma += r.randint(20, 35)
    if suma >= 100:
        k += 1
    arr.append(suma)

i = 80
while i <= 140:
    g = 0
    for _ in arr:
        if _ == i:
            g += 1
    # f.write(str(i) + ' -> ' + str(g) + '\n')
    f.write(str(g) + '\n')
    i += 1
