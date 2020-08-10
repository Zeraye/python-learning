# problem: https://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
import random

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
password = []


def strong():
    length = random.randint(10, 15)
    i = 1

    while i <= length:
        which_sign = random.randint(1, 4)
        if which_sign == 1:
            which_digit = random.randint(0, 9)
            password.append(digits[which_digit])
            i += 1
        elif which_sign == 2:
            which_lowercase = random.randint(0, 25)
            password.append(lowercase[which_lowercase])
            i += 1
        elif which_sign == 3:
            which_uppercase = random.randint(0, 25)
            password.append(uppercase[which_uppercase])
            i += 1
        elif which_sign == 4:
            which_symbol = random.randint(0, 7)
            password.append(symbols[which_symbol])
            i += 1
    return password


def weak():
    length = random.randint(1, 2)
    i = 1

    while i <= length:
        which_sign = random.randint(1, 2)
        if which_sign == 1:
            which_digit = random.randint(0, 9)
            password.append(digits[which_digit])
            i += 1
        elif which_sign == 2:
            which_lowercase = random.randint(0, 25)
            password.append(lowercase[which_lowercase])
            i += 1


def show():
    global length
    times = 0
    while times < length:
        print(password[times], end="")
        times += 1


def main():
    strength = input("How strong password I should generate [strong, weak]:  ")
    if strength == "strong":
        strong()
        show()
    elif strength == "weak":
        weak()
        show()
    else:
        print("Type 'strong' or 'weak'!")
        main()


main()
