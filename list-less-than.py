# problem: https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

x = int(input("Give any number: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in a:
    if number < x:
        print(number)
