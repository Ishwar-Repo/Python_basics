# Loops are useful tool when you want to have code run on every item in a piece of data that has indexes.
from math import factorial

# 1. while loop
counter = 0

while counter < 3:
    print("Counter value = "+str(counter))
    counter+= 1
print("--------------------------------------------------------------------------------")

#Assignment 1 - Print the enters number in descending order
# For this exercise, you will print 10 descending integers starting from 10 and ending at 1 with each integer being 1 less than the last and
# each integer printed on a new line. Create a variable and assign it the integer 10
# Then, print 10 9 8 7 6 5 4 3 2 1  in the output by using a while loop to print numbers while
# the variable does not equal 0.  Use the -= operator to reassign descending values to the variable.

count1 = 10

while count1 > 0 : #(count1 !=0)
    print("Count value = "+str(count1))
    count1-=1
print("--------------------------------------------------------------------------------")

#Assignment 2 -  The total of the entered value and all its preceding numbers.
# Write a program which gets a positive integer from a user using input() and assigns it to a variable.
# The program should then use a while loop to get the sum of all the integers from
# the integer that was entered by the user down to 1.  For example, if the integer entered by the user was 6, the while loop would find the sum of 6, 5, 4, 3, 2, and 1, which is 21.
# At the bottom of your program create two print statements.  One will display the user entered integer and the other will display the sum found by the while loop.

entered_val = 5#int(input("Enter the positive integer value = "))
summed = 0

while entered_val > 0:
    print("Current value of entered_val is = "+str(entered_val))
    summed +=entered_val
    entered_val -=1
print("Total of summed value is = " + str(summed))
print("==================================================while loop")

# 2. for loop

word = "Hello"

for letter in word:
    print(letter)
print("--------------------------------------------------------------------------------")

word1 = "hello world"

for letter in word1:
    print(letter)
print("--------------------------------------------------------------------------------")

#Assignment - Count Of Characters in string
# In a .py file, write a program which calculates the number of characters in a string.
# The string should be entered using input() and assigned to a variable.
# Use print() twice at the end of your program.  The first print() will print the string that the user entered and
# the second print() will display the number of characters in the string.  For example,
# if the user entered the string "hello world", the number of characters would be 11.

enter = "abc"#str(input("Enter the string = "))
count = 0

for char in enter:
    print("Letter is = "+str(char))
    count+=1

print("Total char in entered string = "+str(count))
print("==================================================for loop")

#3. range() function - It returns the sequence of number and
# Usually used for iterating over with a for loop
#It can take 3 arguments - start, stop and step
#and can be used with one, two or all three of them at the same time

#3.1 Using range() with 1 argument
one_input = range(5)

for num in one_input:
    print("Printing the numbers in sequence with 1 argument = "+str(num))
print("Type of the data = "+str(type(one_input)))
print("--------------------------------------------------------------------------------")

#3.2 Using range() with 2 argument
two_input = range(5, 10)

for num1 in two_input:
    print("Printing the numbers in sequence with 2 argument = "+str(num1))
print("Type of the data = "+str(type(two_input)))
print("--------------------------------------------------------------------------------")

#3.3 Using range() with 3 argument
three_input = range(1, 20, 3)

for num2 in three_input:
    print("Printing the numbers in sequence with 3 argument = "+str(num2))
print("Type of the data = "+str(type(three_input)))
print("--------------------------------------------------------------------------------")

three_input = range(20, 1, -3)

for num2 in three_input:
    print("Printing the numbers in sequence with 3 argument = "+str(num2))
print("Type of the data = "+str(type(three_input)))
print("--------------------------------------------------------------------------------")

#Assignment 1
# Write a program that iterates over the integers 1 through 50 using a loop.
# However, for numbers which are multiples of both 3 and 5 print “FizzBuzz” in the output.
# For example, 15 is divisible by both 3 and 5, so instead of printing 15, print "FizzBuzz".
# For numbers which are multiples of 3 but not 5 (such as 42) print “Fizz” instead of the number.
# For the numbers that are multiples of 5 but not 3 (such as 20) print “Buzz” instead of the number.
# All the integers which are not multiples of 3 or 5 should just be printed as themselves.

random_numbers = range(1,51)

for aaa in random_numbers:
    if aaa%3==0 and aaa%5==0:
        print("FizzBuzz = "+str(aaa))
    elif aaa%3==0:
        print("Fizz= "+str(aaa))
    elif aaa%5==0:
        print("Buzz= "+str(aaa))
    else:
        print(aaa)
print("--------------------------------------------------------------------------------")

#Assignment 2
# Create a function which takes one positive integer as its input and returns its factorial.
# To make sure that your function works correctly, you should call it with the inputs 3, 4, and 5 and print what is returned by those calls.
# For those inputs, you should get 6, 24, and 120, respectively.

def fun_of_fact (factnum):
    returned = 1
    for item in range(factnum, 1, -1):
        print("Value of an item = "+str(item))
        returned*=item
        print("Value of an returned = " + str(returned))
    return returned

print("Factorial of given no is = "+str(fun_of_fact(4)))
print("--------------------------------------------------------------------------------")

fact = factorial(5)
print("Factorial of given no is = "+str(fact))
print("--------------------------------------------------------------------------------")