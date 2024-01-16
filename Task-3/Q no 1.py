

# Given a python list and create two lists from it , one with the even numbers and the other with odd numbers 

list = [10,501,22,37,100,999,87,351]

odd_numbers = []
even_numbers = []


for i in list:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print("The even numbers present in the given list are as follows: ")
print(even_numbers)

print("\n The odd numbers present in the given list are as follows: ")
print(odd_numbers)