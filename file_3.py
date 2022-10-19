'''
A program for solving
quadratic equations
'''
a = float(input('Coefficient of quadratic equation: a = '))
b = float(input('Coefficient of quadratic equation: b = '))
c = float(input('Coefficient of quadratic equation: c = '))

x1 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)

print(f'The first root of a quadratic equation: x1 = {x1}')
print(f'The second root of a quadratic equation: x2 = {x2}')

