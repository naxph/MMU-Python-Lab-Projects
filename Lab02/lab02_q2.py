# Design a program that accepts two integers and show their average.

# Input: A,B
# Process: (A + B) / 2
# Output: Average

A = int(input('Enter the first integer: '))
B = int(input('Enter the second integer: '))

avg = (A + B) / 2

result = "The average of the integers {0} and {1} is {2}.".format(A, B, avg)

print(result)