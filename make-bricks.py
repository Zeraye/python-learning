# problem: https://codingbat.com/prob/p118406
import math


def make_bricks(small, big, goal):
    return goal - min(math.floor(goal / 5), big) * 5 <= small
