# problem: https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

print("Welcome to the birthday dictionary. We know the birthdays of:")
print("Albert Einstein")
print("Benjamin Franklin")
print("Ada Lovelace")

name = input("Who's birthday do you want to look up? >> ")

names = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
}

if name == "Albert Einstein":
    print("Albert Einstein's birthday is {}".format(names["Albert Einstein"]))
if name == "Benjamin Franklin":
    print("Benjamin Franklin's birthday is {}".format(names["Benjamin Franklin"]))
if name == "Ada Lovelace":
    print("Ada Lovelace's birthday is {}".format(names["Ada Lovelace"]))


