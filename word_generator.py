#create word generator for hangman (use list)

import random

wordIndex = random.randrange(0,853)

wordbank = open('hangmanwords.txt', 'r')
word = (wordbank.readlines()[wordIndex])
print(word)
