from math import pi

"""This calculates the area of a circle."""
# r = float(input("Enter the radius for the circle here: "))
#
# print("The area of the circle with a radius of " + str(r) + " is " + str(pi * r**2))


"""Input name and print it reversed with a space in between"""
#
# first_name = input("Please enter your first name: ")
# last_name = input("Please enter your last name: ")
#
# print(last_name + " " + first_name)

"""Create an input with 5 comma separated number and make them into a list and
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
#
# filename = input("Please enter the filename that you want: ")
#
# file_ext = filename.split(".")
#
# print("The extension of the file is " + repr(file_ext[-1]))


"""Write a Python program to display the
first and last colors from the following list."""
#
# f_name = input("Please enter your first name: ")
# l_name = input("Please enter your last name: ")
#
# print(l_name + " " + f_name)


"""Write a Python program to
display the examination schedule.
(extract the date from exam_st_date)"""
#
# exam_st_date = (11, 12, 2014)
#
#
# print("The examination will start from: %i/%i/%i"%exam_st_date)


"""Write a Python program that accepts an integer (n) and
 computes the value of n+nn+nnn."""
#
# n = int(input("Enter a number: "))
#
# n1 = int("%s" % n)
# n2 = int("%s%s" % (n, n))
# n3 = int("%s%s%s" % (n, n, n))
#
# calculate = n1 + n2 + n3
# print(calculate)


"""Write a Python program to print the documents (syntax, description
 etc.) of Python built-in function(s)."""
#
# print(abs.__doc__)
# print(repr.__doc__)
# print(next.__doc__)

"""Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module."""
#
# import calendar
#
# y = int(input("Enter the year like ex. 1995: "))
# m = int(input("Enter the month like ex. 5: "))
#
# print(calendar.month(y, m))

"""Write a Python program to print the following here document."""

# its a doc string like above.

"""Write a Python program to calculate number of days between two dates."""
# import datetime
#
# date_one = datetime.date(1995, 5, 6)
# date_two = datetime.date(2020, 8, 4)
#
# difference = date_two - date_one
#
# print(difference)

"""Write a Python program to get the volume of a sphere with radius 6."""
# import math
#
# radius = float(input("Enter the radius of the sphere: "))
#
# cube = math.pow(radius, 3)
#
# volume = float(4/3)*pi*cube
# print("The volume of the this sphere is: {}".format(volume))

"""Write a Python program to get the difference between a given number and 17,
 if the number is greater than 17 return double the absolute difference. """
#
# number_one = int(input("Enter a number: "))
#
# difference = abs(number_one - 17)
#
# if number_one > 17:
#     print(difference * 2)
# else:
#     print("nevermind")

"""Write a Python program to test whether a number
 is within 100 of 1000 or 2000."""
#
# answer = int(input("enter an number close to 1000 or 2000: "))
#
#
# def near_thousand(n):
#     return (abs(1000 - n) <= 100) or (abs(2000 - n) <= 100)
#
#
# print(near_thousand(answer))

"""Write a Python program to calculate the sum of three given numbers,
 if the values are equal then return three times of their sum. """

# number_1 = float(input("Please enter the first number: "))
# number_2 = float(input("Please enter the second number: "))
# number_3 = float(input("Please enter the third number: "))
#
# number_sum = number_1 + number_2 + number_3
#
# if number_1 == number_2 == number_3:
#     print("These numbers cubed is : {}".format(number_sum ** 3))
# else:
#     print("The sum of these numbers is: {}".format(number_sum))

"""Write a Python program to get a new string from a given string where 
"Is" has been added to the front. If the given string already begins with 
"Is" then return the string unchanged."""


# def new_string(str):
#     if len(str) >= 2 and str[:2] == "Is":
#         return str
#     return "Is" + str
#
#
# print(new_string("array"))
# print(new_string("Isarray"))

"""Write a Python program to get a string which
 is n (non-negative integer) copies of a given string."""


# def greater_string(str, n):
#     result = ""
#     for i in range(n):
#         result = result + str
#     return result
#
#
# print(greater_string("this is hayden\n", 10))
# print(greater_string("this is Bazor\n", 10))


"""Write a Python program to find whether a given number (accept from
 the user) is even or odd, print out an appropriate message to the user."""

# user_input = int(input("Please enter a even or odd number: "))
#
#
# def odd_even(number):
#     if number % 2 == 0:
#         print("The number you chose is even.")
#     else:
#         print("This number is odd.")
#
#
# odd_even(user_input)


"""Write a Python program to count the number 4 in a given list"""


# def list_count(n):
#     count = 0
#     for number in n:
#         if number == 4:
#             count += 1
#     return print(count)
#
#
# list_count([2, 3, 4, 4, 6, 4])
# list_count([2, 4, 4, 4, 4, 4])


"""Write a Python program to get the n (non-negative integer) 
copies of the first 2 characters of a given string. 
Return the n copies of the whole string if the length is less than 2."""


# def substring_copy(str, n):
#     flen = 2
#     if flen > len(str):
#         flen = len(str)
#     substr = str[:flen]
#
#     result = ""
#     for i in range(n):
#         result = result + substr
#     return result
#
#
# print(substring_copy('abcdef', 2))
# print(substring_copy('p', 3))

"""Write a Python program to test whether 
a passed letter is a vowel or not. """


user_input = input("Please enter a letter: ")


def vowel_or_not(letter):
    vowel = "aeiou"
    if letter in vowel:
        print("This is a vowel")
    else:
        print("This is a consonant")


vowel_or_not(user_input)
