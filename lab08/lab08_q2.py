mark = []

#inputs
m = float(input('Enter quiz mark: '))
while(m > 0.0):
  mark.append(m)
  m = float(input('Enter quiz mark:'))

#calculate mean
totalMark = 0
for i in range(len(mark)):
  totalMark = totalMark + mark[i]

mean = totalMark / len(mark)


#variance
totalVar = 0
for i in range(len(mark)):
  totalVar = totalVar + (mark[i] - mean)** 2

var = totalVar / len(mark)

print('Mean: ', mean)
print('Variance: ', var)
