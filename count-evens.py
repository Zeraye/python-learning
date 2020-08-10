# problem: https://codingbat.com/python/List-2


def count_evens(nums):
    i = 0
    count = 0
    while i < len(nums):
        if nums[i] % 2 == 0:
            count = count + 1
        i = i + 1
    return count
