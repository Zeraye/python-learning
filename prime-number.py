# problem: https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

num = int(input("Check is you number prime: "))
divider = 1
divisors = []

while divider <= num:
    if num % divider == 0:
        divisors.append(divider)
        divider += 1
    else:
        divider += 1

if len(divisors) == 2:
    print("{} is prime".format(num))
else:
    print("{} is not prime".format(num))
