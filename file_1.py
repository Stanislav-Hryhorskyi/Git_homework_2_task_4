"""
Program that asks the user for two
words and outputs them separated by comma
"""
word_1 = input('Please enter the first word: ')
word_2 = input('Please enter the second word: ')

# variant_1
print(word_1 + ', ' + word_2)
# variant_2
print(word_1, word_2, sep=', ')
# variant_3
print(word_1, ', ', word_2, sep='')
# variant_4
print("{0}, {1}".format(word_1, word_2))
# variant_5
print("%s, %s" % (word_1, word_2))
# variant_6
print(f'{word_1}, {word_2}')
