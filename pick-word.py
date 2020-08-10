# problem: https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
import random

file = open("random-words.txt", "r+")
words = file.readlines()
number = random.randint(1, 267751)
print(words[number])
