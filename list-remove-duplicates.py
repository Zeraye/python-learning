# problem: https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html


def with_loop():
    a = [1, 1, 5, 9, 13, 13, 24, 35]
    for num in a:
        if a.count(num) != 1:
            a.remove(num)
        else:
            pass

    print(a)


def with_sets():
    a = [1, 1, 5, 9, 13, 13, 24, 35]
    a = set(a)
    a = list(a)
    a.sort()
    print(a)


with_sets()
