# problem: https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

numbers = input("Type numbers [first,second,third]: ")
numbers_list1 = numbers.split(",")
numbers_list2 = set(numbers_list1)
numbers_list3 = list(numbers_list2)

print(numbers_list3)

if len(numbers_list3) == 1:
    print(numbers_list3[0])
if len(numbers_list3) == 2:
    if int(numbers_list3[0]) > int(numbers_list3[1]):
        print(numbers_list3[0])
    else:
        print(numbers_list3[1])
if len(numbers_list3) == 3:
    if int(numbers_list3[0]) > int(numbers_list3[1]) and int(numbers_list3[0]) > int(numbers_list3[2]):
        print(numbers_list3[0])
    elif int(numbers_list3[1]) > int(numbers_list3[0]) and int(numbers_list3[1]) > int(numbers_list3[2]):
        print(numbers_list3[1])
    elif int(numbers_list3[2]) > int(numbers_list3[0]) and int(numbers_list3[2]) > int(numbers_list3[1]):
        print(numbers_list3[2])
