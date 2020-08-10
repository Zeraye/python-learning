# problem: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt (question: 2)

num = int(input("Give a number >> "))
output = 1
while num != 0:
    output = output * num
    num = num - 1
print(output)
