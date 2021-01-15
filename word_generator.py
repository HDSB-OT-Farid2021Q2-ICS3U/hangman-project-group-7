
import random

wordIndex = random.randrange(0,853)

# open wordbank txt file
wordbank = open('hangmanwords.txt', 'r')
# get random line
word = (wordbank.readlines()[wordIndex])
# print the line
print(word, end='') # the word in txt file ends w/ \n so the end does not need to have \n
