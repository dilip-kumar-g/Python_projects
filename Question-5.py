# 5) Check if the given string is a palindrome and return in boolean form 

palindrome = input("Enter a word to check if it is a palindrome: ")

palindrome = palindrome.lower()

palindrome = list(palindrome)

x = len(palindrome)

active = True

for i in palindrome:
	if i == palindrome[x-1]:
		x -= 1
	else:
		active = False
		break

if active == True:
	print(active)
	print("The given word is a palindrome")
else:
	print(active)
	print("The given word is not a palindrome")