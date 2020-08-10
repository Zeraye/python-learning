# problem: https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html

word = input("Type any word: ")
word_list = []
word_list_rev = []

i = 0

while i < len(word):
    word_list.append(word[i])
    i += 1
else:
    pass

for char in reversed(word_list):
    word_list_rev.append(char)

if word_list == word_list_rev:
    print("{} is a palindrome".format(word))
else:
    print("{} is not a palindrome".format(word))
