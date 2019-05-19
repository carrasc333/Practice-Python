#!/usr/bin/python
#name = raw_input("Give me your name ")
#print("Your name is "+name )

#age = raw_input("Enter your age ")
#age = int(age)
#print(age)


#age = int(input("Enter your age: "))

import datetime
now = datetime.datetime.now()

name = raw_input("What is your name: ")
age = int(raw_input("What is your age: "))
agey = int(100 - age + now.year)
age1 = int(100 - age)
print(name + " will turn 100 in " + str(age1) + " years, in the year " + str(agey))

