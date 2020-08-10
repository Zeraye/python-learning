# problem: https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

number = int(input("Give any number: "))

if number % 2 == 0:
    print("{} is even".format(number))
elif number % 2 != 0:
    print("{} is odd".format(number))
