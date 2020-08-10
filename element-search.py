# problem: https://www.practicepython.org/exercise/2014/11/11/20-element-search.html

nums = [2, 10, 44, 86, 99, 105, 210]

num = int(input("Give any number: "))

i = 0
x = 100
while i <= len(nums) - 1:
    if num == nums[i]:
        print("{} is contained in list".format(num))
        i = len(nums) + x
    else:
        i += 1

if i != len(nums) + x:
    print("{} is not contained in list".format(num))
