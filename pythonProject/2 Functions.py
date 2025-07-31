#Functions - It is used for reuse the code on different variables and values without having two rewrite it.
def print_five(): #defining the function
    print("This")  #give 4 spaces when we write code for function so that function will understand the code is associated with that same function
    print("is")
    print("an")
    print("example of")
    print("function----------------") # After defining the function, you should have 2 blank lines after it before creating more code - Standard Practice (PEP8)


print_five() # calling the function
print_five()
print_five()
print_five()
print_five() #------------------------------------------------------------------------------------------------------------------------------------

def fun_name():#defining the function
    print(2+2) #given 4 spaces


fun_name()#4 calling the function --------------------------------------------------------------------------------------------------------------

def fun_para(parameter): #function parameter
    print(parameter + 2) #given 4 spaces


fun_para(5)#7 calling the function --------------------------------------------------------------------------------------------------------------


def fun_multipara(p1, p2, p3):
    print(p1 + str(p2) + p3)

first_string="The number " #2 blank lines
fun_multipara(first_string, 9, " is an integer") #The number 9 is an integer --------------------------------------------------------------------------------------------------------------

def default_parameter1(num1=7, num2=8): #default parameters
    print(num1 * num2)


default_parameter1() #56 --------------------------------------------------------------------------------------------------------------------------------

def default_parameter2(num1=7, num2=8): #default parameters with passing an argument
    print(num1 * num2)


default_parameter2(6, 4) #24 --------------------------------------------------------------------------------------------------------------

def default_parameter3(num1=10, num2=8): #default parameters using return with expression
    return num1 * num2 #  print(num1 * num2) --error(unsupported operand type(s) for +: 'NoneType' and 'int')


print(default_parameter3() + 20) #100 --------------------------------------------------------------------------------------------------------------------

#Assignment1
# Create a function called hello_world_printer() which takes no parameters and prints the string "hello world"
# Call the function hello_world_printer()

def hello_world_printer():
    print("\"hello world\"")


hello_world_printer() #"hello world" ------------------------------------------------------------------------------------------------------------------------

#Assignment2
# Create a function called name_printer which takes 1 parameter and prints it
# Create a variable called name and assign it user input().  input()'s message should ask the user to enter their name.
# Call name_printer() with the variable "name" as its argument.

# def name_printer(n1):
#     print(n1)
#
# name=input("Please enter the name = ")
# name_printer(name) #Please enter the name = Ishwar --------------------------------------------------------------------------------------------------------------


#Assignment3
# For this programming challenge, you will be creating a function that calculates the volume of a rectangular prism in cubic feet.  The formula to find the volume of a rectangular prism is
# V = l * w * h where l, w, and h are length, width, and height, respectively.
# First, create three variables representing length, width, and height.   Assign each of them an integer as user input using the input() function and int().
# Next, create a function to calculate the volume of the rectangular prism.  It should have 3 parameters representing length, width, and height and return the volume of a rectangular prism
# calculated using those 3 parameters.
# Finally, use print() to display "The volume of the rectangular prism is [call function  here to calculate volume] cubic feet." in the output.
# You will have to use str() on the function call to be able to concatenate it with strings since it returns an integer.

# length1=int(input("Enter the length = "))
# width2=int(input("Enter the width = "))
# height3=int(input("Enter the height = "))
#
# def rect_prism(L, W,  H):
#     return L * W * H
#
#
# print("The volume of the rectangular prism is = "+str(rect_prism(length1, width2, height3))+" cubic feet")

# #Answer-
# #The volume of the rectangular prism is = 7986 cubic feet --------------------------------------------------------------------------------------------------------------

#Assignment4
# The formula for converting from degrees Celsius to degrees Fahrenheit is as follows:F = 1.8 * C + 32
# Where F is the Fahrenheit temperature and C is the Celsius temperature.
# In a .py file, create a variable and assign it an integer representing a Celsius temperature that is entered as user input().
# input()'s message should prompt the user to enter an integer value.
# For this programming challenge, you will then write a function called Fahrenheit that takes in an integer representing a Celsius temperature as its argument.
# The function will return the Fahrenheit equivalent temperature of that argument to 1 place after the decimal.
# At the end of your program, display the Fahrenheit equivalent in a print statement message formatted like so:
# "The Fahrenheit equivalent of [user entered integer] degrees Celsius is [number returned by function]".
# To make sure that the function works, run your program multiple times and call the function on different user entered integer values both negative and positive.

# def fahrenheit(cel):
#     return (18 * cel + 320) / 10
#
#
# celsius=int(input("Please enter an integer value for degrees celsius = "))
# print("The Fahrenheit equivalent of "+str(celsius)+" degrees Celsius is = "+ str(fahrenheit(celsius)))
#
# def fahrenheit1(cel1):
#     return round ((1.8 * cel1 + 32), 1) # round function is used to round off the value
#
#
# celsius1=int(input("Please enter an integer value for degrees celsius = "))
# print("The Fahrenheit equivalent of "+str(celsius1)+" degrees Celsius is = "+ str(fahrenheit1(celsius1)))

##Answer -
##Please enter an integer value for degrees celsius = 90
##The Fahrenheit equivalent of 90 degrees Celsius is = 194.0

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#importing modules- It contains set of functions that can be useful for many different things to use the function within them, you must import them
# 3 Types of importing modules - 1. Generic imports 2. Function import 3. Universal imports

#1. Generic imports
import random

print(random.randint(1, 10))   ##the value lies bet 1 to 10 -->random=module & randint=function, and it returns the random value on run

#2. Function import
from random import randint

print(randint(10, 15)) #the value lies bet 10 to 15

#3. Universal imports
from random import *

print(random()) #the value lies bet 0.0 to 1.0

#Assignment1
# For this exercise, you will create a program that approximates the number of miles per gallon that a car gets.
# In a .py file, create two variables, one which will hold a randomly generated integer between 10 and 25 (inclusive of both 10 and 25),
# and another which will hold a randomly generated integer between and inclusive of 200 and 400. The first variable represents the number of gallons of gas that the car's fuel tank holds.
# The second variable represents the miles that the car can travel on a full tank before needing a refuel.
# Using the formula miles per gallon (MPG) = miles driven/gallons used, calculate the car's MPG and display it in the output using print().
# Use floor division instead of regular division for this calculation to get an integer instead of a float.
# This will give a realistic approximation of miles per gallon even though floats such as 19.8 round down a large amount when using floor division since sometimes,
# car manufacturers sometimes exaggerate miles per gallon.  In addition, display the values held in the variables you created for gallons of gas in the car's fuel tank
# and miles it can travel on a full tank with two different print statements.

from random import randint
fuel = randint(10, 25)
miles = randint(200, 400)

print("Car can travel = "+str(miles // fuel)+" miles / gallon")
print("The car fuel tank can hold = "+str(fuel)+" gallons")
print("Tha car can travel = "+str(miles)+" miles on full tank")



