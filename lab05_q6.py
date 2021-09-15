# Shape Calculator

import math

print('A - Rectangle')
print('B - Triangle')
print('C - Circle')

shape = str(input('Enter shape: '))

if shape == 'A':
  rectLength = int(input('Enter Length: '))
  rectWidth = int(input('Enter width: '))
  calculation = rectLength * rectWidth
elif shape == 'B':
  triBase = int(input('Enter Base: '))
  triHeight = int(input('Enter Height: '))
  calculation = (1 / 2) * triBase * triHeight
elif shape == 'C':
  circleRadius = int(input('Enter Radius: '))
  calculation = math.pi * circleRadius ** 2
else:
  print('Error. Please enter a valid shape')

outputText = "Total Area = {0}".format(calculation)
print(outputText)