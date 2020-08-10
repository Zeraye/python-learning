import random as r

k = 0
arr = []
while k < 1000000:
    green = 0
    red = 0
    black = 0
    games = 1
    while green == 0:
        number = r.randint(1, 38)
        if 38 >= number >= 37:
            green = green + 1
        if 36 >= number >= 19:
            red = red + 1
        if 18 >= number >= 1:
            black = black + 1
        games = games + 1
    arr.append(games)
    k = k + 1
    # if k % 1000 == 0:
    #    print(k)

print("average")
print(sum(arr)/len(arr))
arr.sort()
print("biggest lose streak")
print(arr[len(arr)-1])
