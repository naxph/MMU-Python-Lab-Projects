# Write a program that accepts a sentence and shows the number of words, the first word and the last word in the sentence

s = input('Enter a sentence: ')

# split()

r = s.split()

print('Number of Words: ', len(r))
print('First Word: ', r[0])
print('Last word: ', r[-1])