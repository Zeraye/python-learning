import random as r

t = 0
p = 5000000
suma = 0
arr = []
while t < p:
    t += 1
    i = 0
    while True:
        if r.randint(1, 2) == 1:
            i += 1
        else:
            break

    suma += pow(2, i)
    arr.append(pow(2, i))
    print('----------------------')
    print(round((t/p)*100, 2), '%')
    print(suma/t)
    arr.sort()
    print('min ', arr[0], 'max', arr[-1])
