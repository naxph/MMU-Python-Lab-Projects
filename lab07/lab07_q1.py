#Write a program that accepts a sentence and count the number of vowels in the text

sentence = input('Enter a sentence: ')
vowel = 'aeiou' #Array 0,1,2,3,4

sentence = sentence.lower #converts to lower case

count = 0
for a in range(len(vowel)):
  for b in range(len(sentence)):
    if(vowel[a]==sentence[b]):
      count+=1

      print('Number of vowels=', count)
