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
