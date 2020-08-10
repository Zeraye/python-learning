# problem: https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
import datetime

age = input("Give your age: ")
age = int(age)
name = input("Give your name: ")

now = datetime.datetime.now()
print("{}, in {} you will celebrate 100th birthday".format(name, now.year + age))

word = input("Give any word: ")
word_repeat_amount = int(input("How many times i should repeat {}: ".format(word)))

i = 1

while i < word_repeat_amount + 1:
    print("Repeat counter: {}. Word: {}".format(i, word))
    i += 1
