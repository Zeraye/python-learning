import math as m
import pandas as pd

with open("it-homework03.txt", "r") as f:
    arr0 = f.read().split('\n')

print(arr0)

i = counter = 0
while i < 150:
    if int(arr0[i][2])*10 + int(arr0[i][3]) == 12:
        counter += 1
    i += 1
print('a) liczba osób urodzonych w grudniu', counter)

i = counter = 0
while i < 150:
    if int(arr0[i][9]) % 2 == 0:
        counter += 1
    i += 1
print('b) liczba kobiet pracujących w biurze', counter)

arr1 = []
i = 0
while i < 150:
    arr1.append(int(arr0[i][0])*10 + int(arr0[i][1]))
    i += 1
print('c) rok w którym urodziło się najwięcej pracowników', 1900 + max(set(arr1), key=arr1.count))

arr2 = []
i = 0
print('d) niepoprawne numery pesel')
while i < 150:
    x = int(arr0[i][0]) + int(arr0[i][1])*3 + int(arr0[i][2])*7 + int(arr0[i][3])*9 + int(arr0[i][4]) + int(arr0[i][5])*3 + int(arr0[i][6])*7 + int(arr0[i][7])*9 + int(arr0[i][8]) + int(arr0[i][9])*3
    y = int(m.fmod(x, 10))
    if y == 0:
        z = 0
    else:
        z = 10 - y
    if int(z) != int(arr0[i][10]):
        arr2.append(arr0[i])
    i += 1
arr2 = sorted(arr2)
for _ in arr2:
    print(_)

arr3 = []
i = 0
while i < 150:
    arr3.append(int(arr0[i][0]))
    i += 1
print('d)\n50 ->', arr3.count(5), '\n60 ->', arr3.count(6), '\n70 ->', arr3.count(7), '\n80 ->', arr3.count(8), '\n90 ->', arr3.count(9))


