import random as r

bad = 0
good = 0
k = 0
while k < 1000000:
    a = r.randint(1, 9)
    b = r.randint(0, 9)
    c = r.randint(0, 9)
    d = r.randint(0, 9)
    if a + b * c * d == 2:
        good += 1
    else:
        bad += 1
    k += 1
    if k % 1000 == 0:
        print(k)

print(good / (bad + good))
