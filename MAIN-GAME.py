# Authors: Dan Grigorof, Ivan Price, Harry Sun
# Date of Creation: January 13, 2021
# Description: A python program of a hangman game, a guessing game where you guess if a letter is in a word. 6 incorrect guesses then the man gets hanged and you lose.
# File Version: 2021-01-19


import os
clear = lambda: os.system('cls')
import random

def win():
    """function for when player wins"""
    print(f"congratulations,you beat the game! You guessed {word}", end='')
def lose():
    """function for when player loses"""
    print(f"you lost the game :( | the correct word was {word}", end='')

def title():
    print('HANGMAN ELITE'.center(30, '*'))

# life drawing system completed 01-18-21
def SixLives():
    print("""               +---+            
              |   
              |
              |
              |
              |
              ========""")
def FiveLives():
    print("""               +---+            
              |   O
              |
              |
              |
              |
              ========""")
def FourLives():
    print("""               +---+            
              |   O
              |   |
              |   |
              |
              |
              ========""")
def ThreeLives():
    print("""               +---+            
              |   O
              |   |
              |   |
              |  /
              |
              ========""")
def TwoLives():
    print("""               +---+            
              |   O
              |   |
              |   |
              |  / \\
              |
              ========""")
def OneLife():
     print("""               +---+            
              |    O
              |   \|
              |    |
              |   / \\
              |
              ========""")


# word generator system completed 01-15-21
wordIndex = random.randrange(0, 853 + 1)

#guessbank is a string because i found it to be easier to work w/ and faster performance wise
guessbank = ''

life = 6

# open wordbank txt file
wordbank = open('hangmanwords.txt', 'r')

# generate random line
word = (wordbank.readlines()[wordIndex])

fixedWord = list(word)[:-1]

clear() # CLEAR OUTPUT

title()

SixLives()

# loop integrated 01-15-21
while True:
    correct = True
# prints line of letters in the word + spaces
    for char in fixedWord:
            if char in guessbank:
                print(char, end='')
            else:
                correct = False
                print('_ ', end='')
    print('')
    if correct == True:
        break
    # input for players guess
    guess = input('enter guess [letter / word] : ')

    clear() # CLEAR OUTPUT

    if guess.lower() + '\n' == word:
        break
    else:
        if guess.lower() not in fixedWord:
            life -= 1
        # life drawings
        title()
        if life == 6:
            SixLives()
        if life == 5:
            FiveLives()
        elif life == 4:
            FourLives()
        elif life == 3:
            ThreeLives()
        elif life == 2:
            TwoLives()
        elif life == 1:
            OneLife()
        elif 0 >= life:
            break
        if guess.lower() not in fixedWord:
            print(f'try again | you have {life} lives left!')
        else:
            print(f'you have {life} lives left!')

        if len(guess) == 1:
            guessbank += guess.lower()

clear() # CLEAR OUTPUT

# when program finds end term -
if 0 >= life:
    lose()
    print("""              +---+
             |   O
             |  \|/
             |   |
             |  / \\
             |
             |
             ========""")
else:
    win()