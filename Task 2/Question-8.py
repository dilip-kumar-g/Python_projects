# 8) compare 2 words and return boolean if it is an anagram 

string1 = input("Enter a word: ")
string2 = input("Now enter another word to check if it is an anagram: ") 

string1 = string1.lower()
string2 = string2.lower()

for i in string1:
	if i in string2:
		continue
	else:
		active = False

active = True

if len(string1) != len(string2):
	active = False
	
if active == True:
	print(active)
	print("Yes, The first word is an anagram of another")
else:
	print(active)
	print("No, The first word is not an anagram of another")