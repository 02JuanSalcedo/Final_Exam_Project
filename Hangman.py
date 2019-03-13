# Hangman
# Juan Salcedo
# 3.7.19

# Importing necessary modules
import random

while True:
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
    guesses_left = 10
    while num < len(answer):
        if guesses_left != 0:

            print(str(guesses_left), " guesses left")
            user_guess = input('Guess a letter: ')
            # Modified after "User input" branch
            user_guess = user_guess.lower()

            # Replaces dashes with user chosen letters
            misses = 0
            for i in range(len(answer)):
                if answer[i] == user_guess:
                    display[i] = user_guess
                    num = num + 1
                else:
                    misses = misses + 1
            print('\n', ' '.join(display))
            print("correct:", num)
            if misses == len(answer):
                guesses_left = guesses_left - 1
            else:
                continue

        else:
            print("You lost!")
            break
    else:
        print('you won')

        # Asks user if they would like to play again
    print('Do you want to play again? yes/no')
    ans = input()
    if ans != 'yes':
        break

