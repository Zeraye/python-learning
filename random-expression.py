import random
file = open('game-challenges.txt', 'r')

exprs = file.readlines()

length = len(exprs)
i = 0
while i < length:
    num = random.randint(0, len(exprs) - 1)
    print(exprs[num])
    exprs.pop(num)
    num = random.randint(0, 1)
    k = 0
    while k < num:
        print('nic')
        k += 1
    i += 1

print('koniec')
