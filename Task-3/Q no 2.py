
# Given a list of numbers, return the no of prime numbers in it and list them 

numbers = [10, 501, 23, 22, 37, 100, 999, 87, 351]

for num in numbers:
    y = int((num / 2) + 1)

    for i in range(2, y):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

