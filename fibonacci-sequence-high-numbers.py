# problem: Emil Lasocha

base = int(input("Base: "))
pow1 = int(input("Power: "))

power = base ** pow1

num = (1 / (5 ** (1/2) )) * ( ( ( ((1+(5 ** (1/2))) / 2) ** (power)) ) - ( ((1-(5 ** (1/2))) / 2) ** (power)  ) )

print(num)
