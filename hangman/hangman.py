from hangman.word_list import word_list
from hangman.hangman_art import stages
from hangman.hangman_art import logo
import random

print(logo)

RANDOM_WORD = random.choice(word_list)
display_array = []
for i in range(len(RANDOM_WORD)):
    display_array.append('_')

lives = 6


def isWin(array):
    if (array.count('_') == 0):
        return True

    return False

def checkLife(number):
    if number == 0:
        return False

    return True


while isWin(display_array) != True and checkLife(lives) == True:
    guess = input('Guess:')
    if guess in RANDOM_WORD:
        indices = [i for i, c in enumerate(RANDOM_WORD) if c == guess]
        for i in indices:
            display_array[i] = RANDOM_WORD[i]

        print(' '.join(display_array))

        if isWin(display_array):
            print("You win!")
        
    else:
        lives = lives - 1
        print(stages[lives])
        print(' '.join(display_array))
        if checkLife(lives) == False:
            print("You lost...")
