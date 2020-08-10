import math as m

# n = int(input())
n = 0
print("n ", n)
x = m.sqrt(m.pow(n, 2) + 1)
print("x ", x)
y = m.sqrt(m.pow(n + 1, 2) + 1)
print("y ", y)
cos = (m.pow(x, 2) + m.pow(y, 2) - 1) / (2 * x * y)
print("cos ", cos)
tg = m.sqrt(1 - m.pow(cos, 2)) / cos
print("tg ", tg)
katr = m.atan(tg)
print("kat w radianach", katr)
kats = m.degrees(katr)
print("kat w stopniach", kats)

n = 0
suma = 0
while n <= 24:
    x = m.sqrt(m.pow(n, 2) + 1)
    y = m.sqrt(m.pow(n + 1, 2) + 1)
    cos = (m.pow(x, 2) + m.pow(y, 2) - 1) / (2 * x * y)
    tg = m.sqrt(1 - m.pow(cos, 2)) / cos
    katr = m.atan(tg)
    kats = m.degrees(katr)
    suma = suma + kats
    n = n + 1

print("odpowiedz ", round(m.tan(m.radians(suma))))
