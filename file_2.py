"""A program that prompts the user
for three integers and prints their product"""

a = int(input('Please input the first integer number: a = '))
b = int(input('Please input the second integer number: b = '))
x = int(input('Please input the third integer number: x = '))

# variant_1
print('The product of three integers is:', a*b*x)
# variant_2
print(f'The product of three integers is: {a*b*x}')
# variant_3
print('The product of three integers is: %d' % (a*b*x))
# variant_4
print('The product of three integers is: {0}'.format(a*b*x))

