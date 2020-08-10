from openpyxl import load_workbook
import math as m

wb = load_workbook("it-homework02.xlsx")

sheet_ranges = wb['Arkusz1']

arr1 = []
arr2 = []
i = 1
while i < 1001:
    a = 'A' + str(i)
    b = 'B' + str(i)
    arr1.append(sheet_ranges[a].value)
    arr2.append(sheet_ranges[b].value)
    i += 1

counter = i = 0
while i < 1000:
    if arr1[i] % arr2[i] == 0 or arr2[i] % arr1[i] == 0:
        counter += 1
    i += 1
print('a) ', counter)

counter = i = 0
while i < 1000:
    if m.gcd(arr1[i], arr2[i]) == 1:
        counter += 1
    i += 1
print('b) ', counter)

i = 0
mirr_arr1 = []
mirr_arr2 = []
while i < 1000:
    num = p = 0
    while p < len(str(arr1[i])):
        num += int(str(arr1[i])[p])
        p += 1
    mirr_arr1.append(num)
    num = p = 0
    while p < len(str(arr2[i])):
        num += int(str(arr2[i])[p])
        p += 1
    mirr_arr2.append(num)
    i += 1

counter = i = 0
while i < 1000:
    if mirr_arr1[i] == mirr_arr2[i]:
        counter += 1
    i += 1
print('c) ', counter)
