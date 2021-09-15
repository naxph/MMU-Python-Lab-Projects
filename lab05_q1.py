# Write a Python program that accepts two numbers and show
# the largest number among them

numberOne = int(input('Enter 1st Number: '))
numberTwo = int(input('Enter 2nd Number: '))

if numberOne > numberTwo:
  result = "{0} is the largest.".format(numberOne)
else:
  result = "{0} is the largest.".format(numberTwo)

print(result)