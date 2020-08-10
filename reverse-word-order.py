# problem: https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

sen = input("Type any sentence: ")

words = sen.split()
words.reverse()
length = len(words)
i = 0

while i <= length - 1:
    print(words[i], end=" ")
    i += 1
