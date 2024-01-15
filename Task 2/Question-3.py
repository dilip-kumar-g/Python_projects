# 3) Pick a string and return as a new string with all vowels removed 

word = input("Enter the word to remove the vowels in it: ")
word = list(word)
vowels = ['a','e','i','o','u']

for i in word:
	if i in vowels:
		word.remove(i)

final_string = ''.join(word)

print(final_string)