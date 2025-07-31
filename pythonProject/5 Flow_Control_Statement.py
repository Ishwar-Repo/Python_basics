#1. if statement
# if True:
#      "Do the stuff here"

veg =str("corn") #str(input("Enter the vegetable name = "))
if veg=="corn":
    print("The entered vegetable is corn")

print("==================================================if statement")

#2. else statement syntax
# if False:
#     "Do the stuff here"
# else:
#     "Do this instead"

veg =str("tom") #str(input("Enter the vegetable name = "))
if veg=="corn":
    print("The entered vegetable is corn")
else:
    print("The entered vegetable is not corn")
print("==================================================else statement")

#3. Nested if and else statement syntax = very important

GPA =4#int(input("Enter the GPA = "))

if GPA>=3.7:
    print("Accepted by approved institution")
    Institution ="y"#str(input("Is institute is qualifying the loan or not? = "))
    if Institution == "y":
        print("Qualifies for the low APR loan")
    else:
        print("Does not qualify fo the loan")
else:
    print("Need Higher GPA to qualify")

print("----------------------------------------------------------------------------------------------------------------------------------")
#Assignment 1
# Professor Fuentes teaches a Python class and uses the following grading scale for all of her exams.
# You work as a teacher's assistant and due to her busy schedule she has requested that you
# write a program which will determine the grades of the class's students.
# Her grading scale is as follows:
# A score of 90 or above is an A
# A score of 80 or above is a B
# A score of 70 or above is a C
# A score of 60 or above is a D
# A score any lower is an F
# For this exercise, start by creating a variable and assigning that variable a student's score as an integer using input().
# Then, using nested if and else statements and the following set of rules, determine and
# then display the student's grade along with their score using print().
# If the student's score is greater than or equal to 90, then the student will receive an A grade.
# Otherwise, if the student's score is greater than or equal to 80, then the student will receive an B grade.
# Otherwise, if the student's score is greater than or equal to 70, then the student will receive an C grade.
# Otherwise, if the student's score is greater than or equal to 60, then the student will receive an D grade.
# Otherwise, the student will receive an F grade.
# Make sure to run your program multiple times and test it with values for each 5 of the different grades
# to make sure that the correct output is displayed for any value entered as a student's score.

students_score = 88 #int(input("Enter the student score = "))
if students_score>=90:
    print("The score is = "+str(students_score)+" hence, received an A grade")
else:
    if students_score>=80:
        print("The score is = "+str(students_score)+" hence, received an B grade")
    else:
        if students_score >= 70:
            print("The score is = "+str(students_score)+" hence, received an C grade")
        else:
            if students_score >= 60:
                print("The score is = "+str(students_score)+" hence, received an D grade")
            else:
                print("The score is = "+str(students_score)+" hence, received an F grade")
print("==================================================Nested if and else statement")

#OR
students_score = 99#int(input("Enter the student score = "))
if students_score>=90:
    print("The score is = "+str(students_score)+" hence, received an A grade")
elif students_score>=80:
    print("The score is = "+str(students_score)+" hence, received an B grade")
elif students_score >= 70:
    print("The score is = "+str(students_score)+" hence, received an C grade")
elif students_score >= 60:
    print("The score is = "+str(students_score)+" hence, received an D grade")
else:
    print("The score is = "+str(students_score)+" hence, received an F grade")
print("==================================================Nested if and else statement")

#4. else-if statement syntax

user_num = 44 #int(input("Enter the integer number = "))
if user_num<0:
    print("Entered number is =  "+str(user_num)+", which less than zero ")
elif user_num ==0:
    print("Entered number is =  "+str(user_num)+", which equal to zero ")
elif 0< user_num <=100:
    print("Entered number is =  "+str(user_num)+", which is 1, 100 or in between")
else:
    print("Entered number is =  "+str(user_num)+", which is above the 100")

print("------------------------------------------------------------------------------------------------------------")
#Assignment
# For this exercise, start by creating a variable and assigning it a randomly generated integer between and inclusive of both 1 and 10
# Then, using your knowledge of if, elif, and else statements, create a program which prints the roman numeral equivalent of the randomly generated number.
# For example, if the randomly generated integer was 9, then the program would say that the roman numeral equivalent of 9 is IX in the output.

from random import randint

random_number = randint(1,10)
print("Auto generated random number = "+str(random_number))
if random_number==1:
    print("Random number is = "+str(random_number)+", which is roman numeral equivalent of 1 is I")
elif random_number==2:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 2 is II")
elif random_number == 3:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 3 is III")
elif random_number == 4:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 4 is IV")
elif random_number == 5:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 5 is V")
elif random_number == 6:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 6 is VI")
elif random_number == 7:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 7 is VII")
elif random_number == 8:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 8 is VIII")
elif random_number == 9:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 9 is IX")
else:
    print("Random number is = " + str(random_number) + ", which is roman numeral equivalent of 10 is X")
print("==================================================else-if statement")

#5. truthy and falsey values
#truthy string: Anything other than an empty string is truthy.
#falsey string: An empty string id falsey

string_example = "abc"#input("Enter any string other than an empty one = ")

if string_example: #string_example != ""
    print("Thank you for entering something")
else:
    print("You did not enter any string")
print("------------------------------------------------------------------------------------------------------------")

#truthy and falsey values for integers, floats an string
# integers --> 0
# floats -----> 0.0
# string -----> ""

print(bool(0))       #False
print(bool(0.0))    #False
print(bool(""))      #False
print(bool(123))   #True
print(bool(0.99))  #True
print(bool(3.99))  #True
print(bool("abc")) #True
print("==================================================truthy and falsey values")