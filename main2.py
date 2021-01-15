
import random

def win():
    print("congradulations,you beat the game")
def lose():
    print(f"you lost the game :( | the correct word was {word}", end='')

wordIndex = random.randrange(0,853)

x = True
guessbank = ''
life = 6

# open wordbank txt file
wordbank = open('hangmanwords.txt', 'r')
# get random line
word = (wordbank.readlines()[wordIndex])
# un-comment the line below to see generated world
#print('reference -', word, end='') # the word in txt file ends w/ \n so the end does not need to have \n

fixedWord = list(word)[:-1]

while x == True:
    for char in fixedWord:
            if char in guessbank:
                print(char, end='')
            else:
                print('_ ', end='')
    print('')

    guess = input('enter guess [letter / word] : ')
    if guess.lower() + '\n' == word:
        break
        #clear
    else:
        if guess.lower() not in fixedWord:
            life -= 1
            if 0 >= life:
                break
            #clear
            print(f'try again | you have {life} lives left!')
        guessbank += guess.lower()
        #clear

if 0 >= life:
    lose()
else:
    win()