# Write a ptogram that accepts three numbers and show the
# largest number among them

numberOne = int(input('Enter 1st Number: '))
numberTwo = int(input('Enter 2nd Number: '))
numberThree = int(input('Enter 3rd Number: '))

if numberOne > numberTwo and numberOne > numberThree:
  result = "{0} is the largest.".format(numberOne)
elif numberTwo > numberOne and numberTwo > numberThree:
  result = "{0} is the largest.".format(numberTwo)
elif numberThree > numberOne and numberThree > numberTwo:
  result = "{0} is the largest.".format(numberThree)
else:
 result = "Error."

print(result)