# problem: https://codingbat.com/prob/p143951


def lone_sum(a, b, c):
    if a == b == c:
        a = 0
        b = 0
        c = 0
    if a == b:
        a = 0
        b = 0
    if a == c:
        a = 0
        c = 0
    if b == c:
        b = 0
        c = 0
    return a+b+c
