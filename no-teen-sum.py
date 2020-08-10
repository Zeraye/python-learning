# problem: https://codingbat.com/prob/p100347


def fix_teen(n):
    if 13 <= n < 15:
        n = 0
    if 16 < n <= 19:
        n = 0
    return n


def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a + b + c
