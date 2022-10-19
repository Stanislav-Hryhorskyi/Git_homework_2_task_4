'''
A program  for calculating
the area of a circle
'''

from math import pi
radius = float(input('Please enter the radius of a circle (linear units): r = '))
area = pi*radius**2
print(f'The area of a circle '
      f'(precision three decimal places):'
      f' S = {area:.3f} square units')

