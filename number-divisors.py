# problem: https://www.practicepython.org/exercise/2014/02/26/04-divisors.html

number = int(input("Enter the number of divisors you are looking for: "))
divider = 1
numbers = []

while  divider <= number:
    if number % divider == 0:
        numbers.append(divider)
        divider += 1
    else:
        divider += 1

print(numbers)
