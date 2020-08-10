# problem: https://codingbat.com/prob/p160533


def close_far(a, b, c):
    if abs(a-b) <= 1:
        if abs(a-c) >= 2:
            if abs(b-c) >= 2:
                return True
    if abs(a-c) <= 1:
        if abs(a-b) >= 2:
            if abs(b-c) >= 2:
                return True
    return False
