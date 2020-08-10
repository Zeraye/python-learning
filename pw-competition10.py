import random as r


k = 0
good = 0
while k < 1000000:
    i = 0
    arr1 = []
    arr = [6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1]
    while i < 5:
        num = r.randint(0, 14 - i)
        arr1.append(arr[num])
        arr.remove(arr[num])
        i += 1
    if arr1.count(6) == 2:
        good += 1
    k += 1

print(good/k)
