import random

w = 8
b = 4
i = 0
t = 0
plus = 0
minus = 0

while t < 1000000:
    while i < 5:
        num = random.randint(1, 100)
        if b == 0:
            w = w - 1
        elif (num % 2) == 0:
            w = w - 1
        elif (num % 2) == 1:
            b = b - 1
        i = i + 1

    #print("White: ", w, " | Black: ", b)

    if b == 0:
        #plus = plus+1
        minus = minus + 1
        pass
    elif (w / b) > 2:
        plus = plus + 1
    else:
        minus = minus + 1
    t = t + 1
    w = 8
    b = 4
    i = 0
    print(t)

g = (plus / (plus + minus) * 100)
print(g)
