'''
check if every element in a list is a string or an integer using lambda function

'''

data = ['helloworld@gnail.com','Think@123','kodambakkam','chennai', 600024]

result = lambda x : type(x)

check = list(map(result,data))

print(data)

j = 0

for i in check:
    if i == str:
        print(data[j],"is a string")
    else:
        print(data[j],"is an integer")
    j +=1