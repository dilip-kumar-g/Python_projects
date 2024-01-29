'''
4. Write python code for Regular expression 

a) Email ID 
b) Mobile number of Bangladesh 
c) Telephone no of USA 
d) 16 character alpha-numeric password composed of alphabets of upper& lower case, numbers and special char

'''

# a) Email ID

import re

def validate_email_id(email_id):
    formated = "^[a-z0-9.-]+@[a-z0-9-]+[.]+[a-z]{2,6}$"
    result = re.search(formated, email_id)
    if result:
        return "SUCCESS : Email ID is valid"
    else:
        return "ERROR : Invalid Email ID"  

email_id = input("Enter the email address to validate: ")

print(validate_email_id(email_id))


# b) checking if the Bangladesh ph num is valid 

import re

def Bangla_mobile_number(mobile_number):
    pattern = "^[1]{1}[0-9]{9}$"
    result = re.search(pattern, mobile_number)
    if result:
        return "SUCCESS : Valid number"
    else:
        return "ERROR : Invalid number"

mobile_number = input("enter the mobile number to verify: ")

print(Bangla_mobile_number(mobile_number))

# c) Telephone no of USA

import re

def validate_US_number(number):
	formatt = "^[0-9]{3}+[-]+[0-9]{4}+[-]+[0-9]{3}$"
	result = re.search(formatt,number)
	if result:
		return "Yes, This phone number is from USA"
	else:
		return "No, This is not a phone number from USA"

number = input("Enter the phone number to validate: ")

print(validate_US_number(number))

# d) 16 character alpha-numeric password composed of alphabets of upper& lower case, numbers and special char

import re

def valid_password(password):
	validation = "^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[@$!%*?&])[A-Za-z0-9@$!%*?&]{16,}$"
	result = re.search(validation,password)
	if result:
		return "Password is Valid"
	else:
		return "Password is Invalid"

password =  input("Enter the password: ")

print(valid_password(password))
