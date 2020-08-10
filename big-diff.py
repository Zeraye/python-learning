# problem: https://codingbat.com/prob/p184853


def big_diff(nums):
    nums.sort()
    return nums[len(nums)-1] - nums[0]