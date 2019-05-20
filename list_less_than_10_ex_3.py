#!/usr/bin/python

#my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 
#for element in my_list:
#	if element < 5:
#		print(element)
		
my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user = int(input("Add a number "))
 
for element in my_list:
	if element < user:
		print(element)