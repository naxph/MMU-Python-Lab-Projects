# Write a Python program that asks the user to enter an
# hour value and a minute value and then displays the two
# values in the format shown below.

hour = int(input('Enter hours: '))
minute = int(input('Enter minutes: '))

time = "Time is {0}:{1} ".format(hour, minute)

print(time)