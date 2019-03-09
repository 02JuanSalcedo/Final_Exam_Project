# Hangman
# Juan Salcedo
# 3.7.19

# Importing necessary modules
import random
import sys

print(dir(random))
print(dir(sys))

# Randomize list and break down into letters
words = ['bread', 'clock', 'mouse', 'banana', 'suitcase', 'cheese', 'mayonnaise']

answer = list(random.choice(words))

print(answer)

# Replace letters with dashes '-'
display = []
display.extend(answer)

for i in range(len(display)):
    display[i] = '-'

# Modified after "Repl_w/_dash" branch
print(' '.join(display))

# Asks user or letters until all are guessed correctly
num = 0

while num > len(answer):
    user_guess = input('Guess a letter: ')
    user_guess = user_guess.lower
    print(num)
