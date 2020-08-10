import random as r

good = 0  # Case where I've got 3 white balls
bad = 0  # Case where I've not got 3 white balls
rep = 100000  # Number of repeats

k = 0
while k < rep:

    w = 0  # White balls
    b = 0  # Black balls
    p = 0
    # Drawing balls three times
    while p < 3:
        a_w = 8  # White balls in box 'A'
        a_b = 20 - a_w  # Black balls in box 'A'
        b_w = 10  # White balls in box 'B'
        b_b = 6  # Black balls in box 'B'

        i = 0
        # Drawing from box 'A' twice
        while i < 2:
            x = r.randint(1, 20 - i)  # I 20 - i, because we're losing 1 ball after drawing
            if 1 <= x <= a_w:  # Drawing white ball from box 'A'
                a_w -= 1
                b_w += 1
            elif a_w + 1 <= x <= 20 - i:  # Drawing black ball from box 'A'
                a_b -= 1
                b_b += 1
            i += 1

        y = r.randint(1, b_w + b_b)  # b_w + b_b = 18 (it have to be like this)
        if 1 <= y <= b_b:
            b += 1
        elif b_b + 1 <= y <= b_w + b_b:
            w += 1

        p += 1

    if w == 3:  # If there's three white balls (I want that case)
        good += 1
    else:  # If there's not thee white balls
        bad += 1

    k += 1

    # Percentage
    print((good / (good + bad) * 100), "%")
    # Probability
    # print(good / (good + bad))
