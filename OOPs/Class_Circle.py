
'''
Python Task 4

1) Create a python class called circle with constructor which will take a List an argument for the task.
The List is [10,501,22,37,100,999,87,351]

2) create proper member variables inside the task if required and use them when necessary. For example for this task create a 
class private vatiable named pi = 3.141

3) From the given List create two class methods Area and perimeter which will be going to calculate Area and perimeter  
'''


class Circle:

	__pi = 3.141


	def __init__(self,number):
			self.numbers = number


	def area_of_circle(self):
		areas = []
		for i in self.numbers:
			area = self.__pi * i * i
			areas.append(area)
		return areas


	def perimeter_of_circle(self):
		perimeters = []
		for i in self.numbers:
			perimeter = 2 * self.__pi * i
			perimeters.append(perimeter)
		return perimeters



if __name__ == "__main__":
	c = Circle([10,501,22,37,100,999,87,351])
	areas = c.area_of_circle()
	perimeters = c.perimeter_of_circle()

	
	given_list = [10,501,22,37,100,999,87,351]
	k = 0	
	for i in given_list:
		print("The area of circle when radius is " + str(i) + " is: ", areas[k])
		print("The perimeter of circle when radius is " + str(i) + " is: ", perimeters[k])
		print()
		k += 1
					
					
					
"""
So in line number 15 I created a class with name 'Circle' and constructor at the line 20 which takes the given list as an argument

In line 17 i placed the class private variable (Encapsulation)

Line 24 and 32 are the methods to calculate the area and perimeter of a circle 

"""