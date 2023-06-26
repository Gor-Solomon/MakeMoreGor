import tensorflow as tf

fileUrl = 'https://www.o-bible.com/download/kjv.txt'
fileName = 'full-bible.txt'
modelFileName = 'text_generator_full_bible.model'

filepath = tf.keras.utils.get_file(fileName, fileUrl)
words = open(filepath, 'r').read().split(' ') # open('names.txt', 'r').read().splitlines()
book = dict()

for w in words:
    chars = ['<S>'] + list(w) + ['<E>']
    for ch1, ch2 in zip(chars, chars[1:]):
        bigram = (ch1, ch2)
        book[bigram] = book.get(bigram, 0) + 1

sortedSet = sorted(book.items(), key=lambda kvp: kvp[1], reverse=True)
for k, v in sortedSet:
 print(f'{k}, {v}')