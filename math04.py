import random as r

games = 0
succ = 0
arr1 = []
while games < 10000:
    arr = []
    k = 0
    while k < 90:
        num1 = r.randint(1, 100)
        num2 = r.randint(1, 100)
        while num1 == num2:
            num2 = r.randint(1, 100)
        num3 = r.randint(1, 100)
        while num1 == num3 or num2 == num3:
            num3 = r.randint(1, 100)
        arr.append(num1)
        arr.append(num2)
        arr.append(num3)
        k += 1

    arr = list(set(arr))
    arr1.append(len(arr))
    if len(arr) == 100:
        succ += 1
    games += 1
print(arr1)
print(max(map(lambda val: ((arr1.count(val)*100)/len(arr1), val), set(arr1))))
p = 1
licznik = 0
mianownik = 0
arr2 = []
while p <= 100:
    arr2.append((arr1.count(p))/len(arr1))
    p += 1
g = 0
while g < 100:
    licznik += arr1[g]*arr2[g]
    g += 1
g = 0
while g < 100:
    mianownik += arr2[g]
    g += 1
print(licznik/mianownik)
