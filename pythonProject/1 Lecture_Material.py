#First Program
print("Hello world")
# this is comment
#----------------------------------------------------------------------------------------

#Mathematical Operations
addition: int=4+5 #9
addition+=10 #19

sub=55-20 #35
sub-=10 #25

multiplication=40*20 #800
multiplication*=20 #16000

division=1000/50 #20
division/=10 #2

bool1=True #True

expo=3**3 #3*3*3=27
expo**=2 #729

flo=10//2 #5
flo//=2 #2

mod=9%7 #2
mod%=2 #0

print("Exponential = ",expo)
print("Addition = ",addition)
print("Subtraction = ", sub)
print("Multiplication = ",multiplication)
print("Division = ",division)
print("Boolean value = ",bool1)
print("Floor_Division = ",flo)
print("Modules = ",mod)
#----------------------------------------------------------------------------------------

#In python, how to print String along with values or variables
print("Addition of 2 & 5 = ",(2+5),"and multiplication of same = ",(2*5)) #Addition of 2 & 5 =  7 and multiplication of same =  10
#----------------------------------------------------------------------------------------

#In Python, we need to take care float values
print("First = ",1.23+2.80) #First =  4.029999999999999
print("Second = ",(123+280)/100) #Second =  4.03
exp=1.23+2.80
print("Third = ",round(exp,4)) #Third =  4.03
#----------------------------------------------------------------------------------------

#In python, we need to take care float values
pasta=16.68
pasta_sauce=6.98
garlic=16.78
italian=15.26
artisan=3.00
meatballs=4.39

total=pasta+pasta_sauce+garlic+italian+artisan+meatballs

print(total) #63.089999999999996
print(round(total,2)) #63.09
#----------------------------------------------------------------------------------------

#Print the string
str1="orange" #o-0,r-1,a-2,n-3,g-4,e-5
print(str1[2]) #2
print("apple"[4]) #e --[a-0,p-1,p-2,l-3,e-4]

#Slicing of string
str2="apricots" #a-0,p-1,r-2,i-3,c-4,o-5,t-6,s-7
print(str2[:3]) #apr --slice the string before 3rd index
print(str2[2:5]) #ric --slice the sting with 2nd index & end before the 5th index
print(str2[4:]) #cots --slice the string with 4th index

#Concatenation Of String
Concatenated="R2"+"_"+"D2" #R-0,2-1,_-2,D-3,2-4
print(Concatenated) #R2_D2 -- String is concatenated
print(Concatenated[3]) #D -- printing the 3rd index char
print(Concatenated[1:4]) #2_D --printing the string with 1st index & ends before the 4th index

#Effects of accessing by index and string slicing on variables
unchanged="forrest_gump" #f-0,o-1,r-2,r-3,e-4,s-5,t-6,_-7,g-8,u-9,m-10,p-11
sliced=unchanged[6:]
print(sliced) #t_gump --printing the string from the 6th index
print(unchanged) #forrest_gump --printing the Concatenated string
print(unchanged[10]) #m --printing the string from the 10th index
print(unchanged) #forrest_gump --printing the Concatenated string

#Assignment
# Create a variable and assign it the string "Just do it!"
# Access the "!" from the variable by index and print() it
# Print the slice "do" from the variable
# Get and print the slice "it!" from the variable
# Print the slice "Just" from the variable
# Get the string slice "do it!" from the variable and concatenate it with the string "Don't ".  Print the resulting string, which should be "Don't do it!" where the "do it!" part is a slice.

assign="Just do it!" #J-0,u-1,s-2,t-3, -4,d-5,o-6, -7,i-8,t-9,!-10
print(assign[10]) #!
print(assign[5:7]) #do
print(assign[8:]) #it!
print(assign[:4]) #Just
print("Don't "+assign[5:]) #Don't do it!
#----------------------------------------------------------------------------------------

#type() function - Finding out which type of data type in it
ex1=True
ex2=123
ex3=44.55

print(type(ex1)) #<class 'bool'>
print(type(ex2)) #<class 'int'>
print(type(ex3)) #<class 'float'>
#----------------------------------------------------------------------------------------

#str() function - String Function-Whatever you want convert into string
ex4=str(False)
ex5=str(789)
ex6=str(99.00)

print(type(ex1)) #<class 'str'>
print(type(ex2)) #<class 'str'>
print(type(ex3)) #<class 'str'>
#----------------------------------------------------------------------------------------

#Escape Sequence - It is a special characters, you use in string which enable to do the things like -
# 1. insert quotes within the sting
# 2. different part of string on different line in o/p

#First- [\t] - Used for make horizontal space
print("This\tis\ta\tlot\tof\tspace") #This	is	a	lot	of	space

#Second- [\n] - Used for new line
print("line one\nline two")
#line one
#line two

#Third-  [\'] and [\"] - Used for quotes
print("\"do it or not\"")  #"do it or not"
print("\'do it or not\'") #'do it or not'

#Fourth-  [\\] - Used for backslash
print("all escape sequence contains \\") #all escape sequence contains \

#Assignment
# Create a variable and assign it a float
# Use print() and type() to print the data type of the variable in the output
# Use str() on the variable from step 1 and concatenate it with the string " is a float." then use print() to display the result
# print() the string "Hello, I'm [name], it's nice to meet you!" including quotes (you will need to use the \' or \" escape sequence depending on whether you enclose your strings in single quotes or double quotes.)

v1=89.99
print(type(v1)) #<class 'float'>
print(str(v1)+" is a float") #89.99 is a float
print("\"Hello, I'm Ishwar Suranje, it's nice to meet you!\"") #"Hello, I'm Ishwar Suranje, it's nice to meet you!"

#Print the Asterisk Triangle
print("*******\n *****\n  ***\n   *")
# *******
#  *****
#   ***
#    *
#----------------------------------------------------------------------------------------

#input() function -- It is similar like scanner class in java

# name=input("Please enter your name") #Please enter your nameIshwar
# print("Your name is : "+name) #Your name is : Ishwar
# print(type(name)) #<class 'str'>

# num=input("Please enter your favorite number") #Please enter your favorite number9
# print("Your favorite number  is : "+num) #Your favorite number  is : 9
# print(type(num)) #<class 'str'>

#Assignment
# In a .py file, create a program and use input() three times to get answers to the following questions from a user.  Store each of the answers in a variable.
# What is your name?
# What is your quest?
# What is your favorite color?
# Then, concatenate everything into a string within a print() statement with the form "So your name is [name], your quest is [quest], and your favorite color is [color]."

# name1 = input("What is your name?")
# que = input("What is your quest? ")
# color= input("What is your favorite color?")
# print("So your name is: "+name1+", your quest is: "+que+", and your favorite color is: "+color)
#----------------------------------------------------------------------------------------

#int() function - you can convert into integer
# user_int=int(input("Please enter the any integer"))
# print(user_int)
# print(type(user_int))

#int("number3rs4nd$ymbol!") --error (invalid literal for int() with base 10: 'number3rs4nd$ymbol!')
#int("1.59") --error (invalid literal for int() with base 10: '1.59')
#int(11.9) -- 11
#int("10.1+9.3") -- error ( invalid literal for int() with base 10: '10.1+9.3')
#int(10.1+9.3) --19

# ex_int=int(input("Please enter the integer value = ")) #Recommended one
# print(ex_int + 10)
#
# ex_int=input("Please enter the integer value = ")
# print(int(ex_int) +10)

#----------------------------------------------------------------------------------------

#float() function - you can convert into float
user_float=float(input("Please enter the any float number ="))
print(user_float)
print(type(user_float))

#float("number3rs4nd$ymbol!") --error (could not convert string to float: 'number3rs4nd$ymbol!')
#float("1") --1.0
#float(1) -- 1.0
#float("10+9") -- error ( could not convert string to float: '10+9')
#float(10+9) --19.0
#----------------------------------------------------------------------------------------

