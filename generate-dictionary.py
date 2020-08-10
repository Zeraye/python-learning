# problem: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt (question: 2)

num = int(input("Give a number >> "))
dic = {}
i = 1
while i <= num:
    dic.update({i: i*i})
    i = i + 1

print(dic)
