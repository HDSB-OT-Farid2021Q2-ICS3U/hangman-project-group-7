
import random


wordIndex = random.randrange(0,853)
x = True
guessbank = []
# open wordbank txt file
wordbank = open('hangmanwords.txt', 'r')
# get random line
word = (wordbank.readlines()[wordIndex])
# print the word
print(word, end='') # the word in txt file ends w/ \n so the end does not need to have \n

splitWord = list(word)
fixedWord = splitWord[:-1]
print(''.join(fixedWord))
#
length = len(word)
blank = []
for x in range(0,length):
    blank.append('___')
print(blank)
killswitch = True
while killswitch == True:
    guess = input("Enter your guess [a letter] : ") # The guess from the player
    guessL = guess.lower() #convert to lower case so it can take captilazied input
    position = -1
    killswitch1 = True
    while killswitch1 == True:
        for x in word:
            position += 1
            if guessL == x:
                print("Congradulations, you found a correct characer! ")
                blank[position] = guessL
                print(blank)
            if blank == word:
                print("congradulations,you beat the game")
                killswitch = False
