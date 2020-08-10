# problem: https://www.practicepython.org/exercise/2014/12/06/22-read-from-file.html

txt1 = open("names-list.txt", "r+")
names = txt1.readlines()
names = set(names)
names = list(names)

txt1.seek(0)
new_names = txt1.readlines()

i = 0
while i < len(names):
    print("Amount: {} | Name: {}".format(new_names.count(names[i]), names[i]))
    i += 1
