# 4) No of unique characters in a string 

password = input("Enter a word to find the no of unique characters in it: ")

password = password.lower()
unique = ''

for i in password:
	if i not in unique:
		unique = unique + i


print("Total no of unique characters present in the string are: " + str(len(unique)))
print(list(unique))