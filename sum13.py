# problem: https://codingbat.com/prob/p167025


def sum13(nums):
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            nums[i] = 0
            if i + 1 < len(nums):
                nums[i + 1] = 0
        i = i + 1
    return sum(nums)
