# problem: https://codingbat.com/prob/p179960


def round10(num):
    rest = num%10
    if 0 <= rest < 5:
        num = num - rest
    if 5 <= rest <= 9:
        num = num + (10 - rest)
    return num


def round_sum(a, b, c):
    a = round10(a)
    b = round10(b)
    c = round10(c)
    return a+b+c
