# problem: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt (question: 6)
import math as m
C = 50
H = 20
D = 0
Q = float(m.sqrt((2 * C * D) / H))

array_q = []
array_d = int(input("Give numbers >> "))
i = 0
while i < len(array_d):
    D = array_d[i]
    array_d[i] = Q
    i = i + 1

print(array_q)
