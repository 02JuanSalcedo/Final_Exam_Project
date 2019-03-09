# Hangman
# Juan Salcedo
# 3.7.19

# Importing necessary modules
import random
import sys

print(dir(random))
print(dir(sys))

# Randomize list and break down into letters
words = ['bread', 'clock', 'mouse', 'banana', 'suitcase', 'kitten', 'jupiter', 'bucket', 'cake', 'goose']

random.choice(words)

answer = list(random.choice(words))

# Replace letters with dashes '-'
display = []
display.extend(answer)

for i in range(len(display)):
    display[i] = '-'

# Modified after "Repl_w/_dash" branch
print(' '.join(display))

# Asks user or letters until all are guessed correctly
num = 0

while num < len(answer):
    user_guess = input('Guess a letter: ')
    # Modified after "User input" branch
    user_guess = user_guess.lower()
    print(num)

    # Replaces dashes with user chosen letters
    for i in range(len(answer)):
        if answer[i] == user_guess:
            display[i] = user_guess
            num = num + 1

    print(' '.join(display))
