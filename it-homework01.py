with open("it-homework01.txt", "r") as f:
    arr0 = f.read().split('\n')

i = x = 0
while i < 1000:
    if int(arr0[i]) % 2 == 0:
        x += 1
    i += 1

print("a) ", x)

arr1 = []
i = x = y = 0
while i < 1000:
    while x < len(arr0[i]):
        y += int(arr0[i][x])
        x += 1
    arr1.append(y)
    x = y = 0
    i += 1

for element in arr1:
    if element == sorted(arr1)[0]:
        print("b) liczba o najmniejszej sumie cyfr ", arr0[arr1.index(element)])
    if element == sorted(arr1)[-1]:
        print("liczba o największej sumie cyfr", arr0[arr1.index(element)])

arr2 = []
i = x = 0
while i < 1000:
    while x + 1 < len(arr0[i]):
        if int(arr0[i][x]) < int(arr0[i][x+1]) and x + 2 == len(arr0[i]):
            arr2.append(arr0[i])
            x = 0
            break
        elif int(arr0[i][x]) < int(arr0[i][x+1]):
            x += 1
        else:
            x = 0
            break
    i += 1

print("c) ", *arr2)

f.close()
