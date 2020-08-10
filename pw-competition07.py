import random as r

t = 0
arr = []
pozytywne = 0
while t < 100000:
    i = 0
    p = 0
    arr = []
    while p < 4:
        arr.append(r.randint(1, 6))
        p += 1
    if len(arr) != len(list(set(arr))):
        pozytywne += 1
    t += 1

print(pozytywne/100000)
