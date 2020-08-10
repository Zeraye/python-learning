# problem: https://codingbat.com/prob/p119308


def has22(nums):
    i = 0
    while i + 1 < len(nums):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
        i = i + 1
    return False
