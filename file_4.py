'''
A program for calculating
the sum of the character codes
of an entered 10-character phrase
'''

phrase = input('Enter a phrase '
               'consisting of '
               '10 characters: ')
while len(phrase) != 10:
    print('This phrase don\'t '
          'consist of 10 '
          'characters!!!')
    phrase = input('Enter a phrase '
                   'consisting '
                   'of 10 characters: ')

amount = 0
for character in phrase:
    amount += ord(character)

print('The sum of the ASCII '
      'codes of the characters '
      'of the entered string: ',
      amount
      )
