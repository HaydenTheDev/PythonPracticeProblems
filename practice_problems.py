from math import pi

# """This calculates the area of a circle."""
# r = float(input("Enter the radius for the circle here: "))
#
# print("The area of the circle with a radius of " + str(r) + " is " + str(pi * r**2))


# """Input name and print it reversed with a space in between"""
#
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
#
# print(last_name + " " + first_name)

# """Create an input with 5 comma separated number and make them into a list and
# a tuple."""
# values = input("Please input 4 values separated by commas: ")
#
# list = values.split(',')
# tuple = tuple(list)
#
# print('List : ', list)
# print('Tuple : ', tuple)

"""Write a Python program to accept a filename 
from the user and print the extension of that"""

filename = input("Please enter the filename that you want: ")

file_ext = filename.split(".")

print("The extension of the file is " + repr(file_ext[-1]))

