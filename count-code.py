# problem: https://codingbat.com/prob/p186048


def count_code(str):
    i = 0
    count = 0
    while i + 3 < len(str):
        if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
            count = count + 1
        i = i + 1
    return count
