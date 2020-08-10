import math as m


def liczenie(x):
    a = 1/x
    return a


k = 1
p = 1000000
wynik = 0
while k < p:
    wynik += liczenie(k)
    # wynik *= liczenie(k)
    k += 1
    print((str(m.floor((k*100)/p)) + "%"))

print(wynik)
