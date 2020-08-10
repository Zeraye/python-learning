import random as r

p = 70
k = 20
exe = []
i = 0
while True:
    n = r.randint(1, p - i)
    exe.append(n)
    exe = list(set(exe))
    if len(exe) >= 20:
        break
    i += 1

print(exe)
