# problem: https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html


def with_loops():
    import random

    list_a = []
    list_b = []
    list_c = []

    len_a = random.randint(1, 30)
    i = 0

    while len_a >= i:
        list_a.append(random.randint(1, 100))
        i += 1
    else:
        pass

    len_b = random.randint(1, 30)
    i = 0

    while len_b >= i:
        list_b.append(random.randint(1, 100))
        i += 1
    else:
        pass

    for number_a in list_a:
        for number_b in list_b:
            if number_a == number_b:
                list_c.append(number_a)
            else:
                pass

    for number_c in list_c:
        if list_c.count(number_c) > 1:
            list_c.remove(number_c)
        else:
            pass

    print("List a: ", list_a)
    print("List b: ", list_b)
    print("Repeated numbers: ", list_c)


def with_sets():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = [num_a for num_a in set(a) for num_b in set(b) if num_b == num_a]

    print(c)


with_sets()
