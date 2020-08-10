# problem: https://codingbat.com/prob/p174314


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    x = 0
    count = 0
    if len(a) <= len(b):
        while x < len(a):
            if a[x] == b[len(b) - len(a) + x]:
                count = count + 1
            x = x + 1
        if count == len(a):
            return True
        else:
            return False
    elif len(a) > len(b):
        while x < len(b):
            if b[x] == a[len(a) - len(b) + x]:
                count = count + 1
            x = x + 1
        if count == len(b):
            return True
        else:
            return False
