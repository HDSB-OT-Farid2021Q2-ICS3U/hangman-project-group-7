
import random

def win():
    print("congradulations,you beat the game")

wordIndex = random.randrange(0,853)

x = True
guessbank = ''

# open wordbank txt file
wordbank = open('hangmanwords.txt', 'r')
# get random line
word = (wordbank.readlines()[wordIndex])
# print the word
print('reference -', word, end='') # the word in txt file ends w/ \n so the end does not need to have \n
#=================================
splitWord = list(word)
fixedWord = splitWord[:-1]
#=================================

while x == True:
    for char in fixedWord:
            if char in guessbank:
                print(char, end='')
            else:
                print('_ ', end='')
    print('')

    guess = input('enter guess [letter / word] : ')
    if guess.lower() + '\n' == word:
        x = False
        #clear
    else:
        print('try again')
        guessbank += guess.lower()
        #clear

win()