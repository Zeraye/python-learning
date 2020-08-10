import random as r
import math as m

n = 12
sd = 2 * n + 1  # sides of polygon
i = 0
isc = 0  # number of isosceles triangles
while i < 1000000:  # number of tries
    i += 1

    a = 1
    b = 1
    while b == a:
        b = r.randint(2, sd)
    c = b
    while c == b:
        c = r.randint(2, sd)

    # print(a, b, c)

    if abs(a - b) <= n:
        ab = abs(a - b) - 1
    else:
        arr = [a, b]
        k = m.ceil(max(arr) / (2 * min(arr)))
        ab = abs(a - b) - 1 - k

    if abs(a - c) <= n:
        ac = abs(a - c) - 1
    else:
        arr = [a, c]
        k = m.ceil(max(arr) / (2 * min(arr)))
        ac = abs(a - c) - 1 - k

    if abs(b - c) <= n:
        bc = abs(b - c) - 1
    else:
        arr = [b, c]
        k = m.ceil(max(arr) / (2 * min(arr)))
        bc = abs(b - c) - 1 - k

    # ab = abs(ab)
    # ac = abs(ac)
    # bc = abs(bc)
    #
    # print(ab, ac, bc)

    if ab == ac == bc:
        isc += 1
        # check = True
    # else:
    #     check = False
    #
    # print(check)

print(n, '->', isc * 100 / i, '%')
n += 1
