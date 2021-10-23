f = open('vehicles.txt', 'r')
lines = f.readlines()
count = 0

for line in lines:
  if(line.find('car') != -1):
    count += 1
    
print(f'"Car" count: {count}')

f.close()