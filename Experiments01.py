# Gives 1.5 times pay raise if hours worked is above 40
# Gives an error message if the user enters anything other than a number.


try:
 hours = int(input('Enter the number of hours you have worked: '))
 rate = int(input('Enter your pay rate: '))

 if hours > 40 :
  pay = hours * (rate * 1.5)
  print(pay)
 else :
  pay = hours * rate
  print(pay)

except:
  print('Error. Please enter a number')