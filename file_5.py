'''
A program that outputs the text
entered by the user in reverse order
'''

text = input('Please enter some text: ')

# variant_1
reverse_text = text[::-1]
print('Text entered by the user is output in reverse order:', reverse_text)

# variant_2
reverse_text = ''
for char in text:
    reverse_text = char + reverse_text
print(f'Text entered by the user is output in reverse order: {reverse_text}')

# variant_3
reverse_text = ''
for var in range(len(text)-1, -1, -1):
    reverse_text += text[var]
print('Text entered by the user is output in reverse order: {0}'.format(reverse_text))

