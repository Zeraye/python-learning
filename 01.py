import math as m
x = 1
y = 1
z = 1
while x < 40:
    y = 0
    z = 0
    print(x)
    while y < 40:
        z = 0
        while z < 40:
            if m.pow(3, x) + m.pow(7, y)*z == 2020:
                print(x, y, z)
            else:
                z += 1
        y += 1
    x += 1
