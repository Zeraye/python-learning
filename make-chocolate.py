# problem: https://codingbat.com/prob/p190859


def floor(n):
    res = int(n)
    return res if res == n or n >= 0 else res-1


def make_chocolate(small, big, goal):
    a = goal/5
    a = floor(a)
    if a > big:
        a = big
    goal = goal - 5*a
    if small >= goal:
        return goal
    return -1