# 7) Take a string and return the most frequent character 

string = input("Enter a string to find its most frequent character: ")
string = string.split(' ')
string = ''.join(string)
hash = {}

for i in string:
	if i not in hash:
		hash[i] = 1
	else:
		hash[i] += 1
print(hash)

values = list(hash.values())

y = max(values)

repeated =[]

for key,value in hash.items():
	if value == y:
		repeated.append(key)

print("The most frequent character in the string are as follows: "+ "\n\t" +str(repeated))
