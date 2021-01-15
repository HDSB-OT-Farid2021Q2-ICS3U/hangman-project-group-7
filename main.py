
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
