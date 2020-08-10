# problem: https://edabit.com/challenge/NtsqbRPqtPYhR8tJe


def blocks(a):
    total = int(3 * (a - 1) + 5 + ((7 + (a - 1)) / 2) * (a - 1))
    if a == 0:
        total = 0
    return total


print(blocks(0))
