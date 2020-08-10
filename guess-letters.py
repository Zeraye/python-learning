# problem: https://www.practicepython.org/exercise/2017/01/02/31-guess-letters.html

letters = ["E", "V", "A", "P", "O", "R", "A", "T", "E"]
blanks = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
guesses = []

for blank in blanks:
    print(blank, end=" ")

while letters != blanks:
    guess = input("\nGuess a word! Type big letter: ")
    i = 0
    for element in guesses:
        if guess == element:
            print("You have already typed this letter!")
            i = 3
            break
    while i < len(letters):
        if guess == letters[i]:
            blanks[i] = guess
            guesses.append(guess)
        i += 1
    for blank in blanks:
        print(blank, end=" ")
