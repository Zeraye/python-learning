# problem: https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

a = [5, 10, 15, 20, 25]
b = []

length = len(a) - 1

b.append(a[0])
b.append(a[length])

print(b)
