import os
import random

def win():
    """function for when player wins"""
    print(f"congradulations,you beat the game you guessed {word}", end='')
def lose():
    """function for when player loses"""
    print(f"you lost the game :( | the correct word was {word}", end='')
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


#random number generator
wordIndex = random.randrange(0, 853 + 1)

#guessbank is a string because i found it to be easier to work w/ and faster performance wise
guessbank = ''
life = 6

# open wordbank txt file
wordbank = open('hangmanwords.txt', 'r')
# get random line
word = (wordbank.readlines()[wordIndex])
# un-comment the line below to see generated world
print('reference -', word, end='')

fixedWord = list(word)[:-1]

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
    if guess.lower() + '\n' == word:
        break
    else:
        if guess.lower() not in fixedWord:
            life -= 1
            #insert live drawing if/else statments here
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
            #-------------------------------------------
            print(f'try again | you have {life} lives left!')
        if len(guess) == 1:
            guessbank += guess.lower()

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