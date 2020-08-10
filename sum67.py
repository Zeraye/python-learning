# problem: https://codingbat.com/prob/p108886


def sum67(nums):
    i = 0
    t = 0
    while i < len(nums):
        if nums[i] == 6:
            t = i
            nums[t] = 0
            while nums[t + 1] != 7:
                nums[t + 1] = 0
                t = t + 1
            if nums[t + 1] == 7:
                nums[t + 1] = 0
        i = i + 1
    return sum(nums)
