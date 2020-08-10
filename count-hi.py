# problem: https://codingbat.com/prob/p167246


def count_hi(str):
    count = 0
    i = 0
    while i + 1 < len(str):
        if str[i] == 'h' and str[i + 1] == 'i':
            count = count + 1
        i = i + 1
    return count
