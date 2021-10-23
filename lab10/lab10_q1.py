# read the text file

f = open('data.txt', 'r')
'''
used to open a file
takes 2 arguments
1st argument: path
2nd argument: mode of operation(optional)

readlines()
- read the file line by line and puts into a list
-returns a list of lines

'''
lines = f.readlines()

count= 0

for line in lines:
  count += 1

print(f'Line count: {count}')
print(f'First line: {lines[0]}')
print(f'Last line: {lines[-1]}')

f.close()