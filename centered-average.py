# problem: https://codingbat.com/prob/p126968


def centered_average(nums):
    nums.sort()
    nums.remove(nums[0])
    nums.remove(nums[len(nums) - 1])
    nums = list(set(nums))
    return sum(nums) / len(nums)
