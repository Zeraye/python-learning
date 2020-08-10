a = 5000
i = 0
s = 0
while i < 12:
    i += 1
    s = 0
    s += a * 0.008
    s += a
    a = s

print(s)
