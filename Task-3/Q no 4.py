
# find the sum of first and last digit of an integer 


no = input("Enter any number that is greater than one digit: ")

no = list(str(no))
no[0] = int(no[0])
no[-1] = int(no[-1])
sum = no[0] + no[-1]

print("The sum of first and last digit of the given number is: " + str(sum))