# problem: https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
import random

file = open("random-words.txt", "r+")
words = file.readlines()
number = random.randint(1, 267751)
number = 260888

new_word = list(words[number])
new_word.remove(new_word[-1])
print(new_word)

blanks = []
guesses = []
times = 0
left = 6
i = 0

while i < len(new_word):
    blanks.append("_")
    i += 1

for blank in blanks:
    print(blank, end=" ")
while left > 0:
    guess = input("\nType a big letter: ")
    i = 0
    while i < len(new_word):
        for letter in guesses:
            if guess == letter and i == 0:
                print("LETTER DOUBLED")
                guess = "random_word"
                i = len(new_word) - 2
        if guess == new_word[i]:
            guesses.append(guess)
            blanks[i] = guess
        elif i == len(new_word) - 1:
            times += 1
        i += 1
        print("WHILE")

    for blank in blanks:
        print(blank, end=" ")

    print("\n", guesses)

    left = 6 - times

    print("You have {} incorrect guesses left".format(left))
