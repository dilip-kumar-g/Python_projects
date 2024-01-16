# 9) Take a string and return the no of words in it 


string = input("Enter a sentence to check the no of words in it: ")

string = string.split(' ')

print(string)
print("The total no of words in the string are: "+ str(len(string)))
