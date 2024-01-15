# 1) Total no of vowels and count of each vowel in the given string 


given_string = 'Guvi Geeks network private limited'
string = given_string.lower()
vowels = ['a','e','i','o','u']
vowels_present = []
for i in given_string:
	if i in vowels:
		vowels_present.append(i)

print('Total no of vowels present in the given string are: '+ str(len(vowels_present)))


for i in vowels:
	print('No of '+ str(i) +"'s present in the string are: " + str(vowels_present.count(i)))