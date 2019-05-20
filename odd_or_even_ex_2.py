#!/usr/bin/python

num = int(input("Enter a number to check: "))
check = int(input("Enter a second number to divide by: "))

if num == 0:
	print("You entered " + str(num))
elif num % 4 == 0:
	print(str(num) + " is an even number and multiples of 4")
elif num % 2 == 0:
	print(str(num) + " is an even number and multiples of 2")
else:
	print(str(num) + "You have an odd number")
	
if num % check == 0:
	print(str(num) + " divides evenly into " + str(check))
else: 
	print(str(num) + " does not divide evenly into your first number " + str(check))
	
	

	
