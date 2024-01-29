'''

create fibonacci series until 50 using lambda func in python

'''

def fibonacci_series(n):

    fibo_series = [0, 1]

    any(map(lambda _: fibo_series.append(sum(fibo_series[-2:])), range(2, n)))

    return fibo_series[:n]

n = int(input("Enter the number to find the fibnacci series: ")) 

fibo_series = fibonacci_series(n)

print(fibo_series[2:n])

'''

In this lambda function i have not used any arguments coz i am taking the postional value of the running list, so inserted _

for  the expression bascially i m trying to append the addition of last two items in the running list until the specified number 

the lambda function is mapped with the list and the expression , and used any() so that the value keeps iterating 

'''

