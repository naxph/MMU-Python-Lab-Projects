# Design a program that accepts a number respresenting a 
# reading of a thermostat in Celcius and show the result
# as its equivelant.

# Input: C
#Process: (9 / 5 * C) + 32
#Output: F

C = int(input('Enter the temperature in Celsius: '))

F = (9 / 5 * C) + 32

result = "The temperature in Farenheight is {0}".format(F)

print(result)