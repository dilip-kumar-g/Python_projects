

# Given a list of integers, find the first non repeating element in the given list 

list1 = input("Enter the list of numbers seperated by comma: ")

list1 = list1.split(',')

list_hash = {}

for i in list1:
    if i not in list_hash:
        list_hash[i] = 1
    else:
        list_hash[i] += 1

values = list(list_hash.values())
end_values = []

for x,y in list_hash.items():
	if y == 1:
		end_values.append(x)


print("The first non repeating character in the given list is: " + str(end_values[0]))

    