import random

k = 0
succ = 0
while k < 1000000:
    x = []
    y = []
    i = 0
    while i < 3:
        x.append(random.randint(0, 5))
        y.append(random.randint(0, 5))
        i += 1
    if x[0] == y[0] or x[1] == y[1] or x[2] == y[2]:
        succ += 1
    k += 1

print((succ * 100) / k)
