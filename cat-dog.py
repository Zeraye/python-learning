# problem: https://codingbat.com/prob/p164876


def cat_dog(str):
    cat = 0
    dog = 0
    count_cat = 0
    count_dog = 0

    while cat + 2 < len(str):
        if str[cat] == 'c' and str[cat + 1] == 'a' and str[cat + 2] == 't':
            count_cat = count_cat + 1
        cat = cat + 1

    while dog + 2 < len(str):
        if str[dog] == 'd' and str[dog + 1] == 'o' and str[dog + 2] == 'g':
            count_dog = count_dog + 1
        dog = dog + 1

    if count_cat == count_dog:
        return True
    else:
        return False
