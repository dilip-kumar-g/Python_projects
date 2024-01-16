# Duplicates in the given python lists (three lists)

list1 = [2,5,7,3,11,4,56,76,89]
list2 = [7,68,2,33,89,21,54,33,67]
list3 = [55,2,20,7,45,67,89,11,56]

duplicate = []
for i in list1:
	while i in list2 and i in list3:
		duplicate.append(i)
		break


if not duplicate:
	print("The given lists has no duplicate values")
else:
	print("The duplicate values present in all the given lists are as follows: " + "\n" + str(duplicate))


