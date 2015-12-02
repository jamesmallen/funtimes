# If ABCDEFGHIJKLMNOPQRSTUVWXYZ equals 1234567891011121314151617181920212223242526
# Then KNOWLEDGE = 96%
# And HARD WORK = 98%
# But ATTITUDE = 100%

# What else adds up to 100%?

import re

# words_file = '/usr/share/dict/words'
words_file = 'en-x-basic.txt'


def score(letter):
    return ord(letter.upper()) - 64

with open(words_file) as f:
    for word in f:
        word = word.strip()
        word_score = sum([score(letter) for letter in word if re.match(r'[a-zA-Z]', letter)])
        if word_score == 100:
            print(word)
