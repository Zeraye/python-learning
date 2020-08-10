# problem: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt (question: 1) 

i = 2000
tb = []
while i <= 3200:
    if i % 7 == 0 and i % 5 != 0:
        tb.append(i)
    i = i + 1

i = 0
while i < len(tb):
    print(tb[i], end=', ')
    i = i + 1
