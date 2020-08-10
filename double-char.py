# problem: https://codingbat.com/prob/p170842


def double_char(str):
    l = len(str)
    word = ""
    i = 0
    while i < l:
        word = word + str[i] + str[i]
        i = i + 1
    return word
