
import time # this imports the time module for the implementation of time stamp

# 1 ) below function is to create a txt file with current time stamp as the content 

def create_file(name,data):
    file = open(name,"w")
    file.write(data)
    return file

# 2) below function is to read the contents in the created file which is created with time stamp

def read_file(name):
    file = open(name,"r")
    return file.read()

print(create_file('current_time.txt',str(time.asctime())))
print(read_file('current_time.txt'))
