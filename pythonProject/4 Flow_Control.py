#Comparison Operator & Boolean Operators

#Comparison Operator - There are 6 types -
# 1. >
# 2. <
# 3. >=
# 4. <=
# 5. !=
# 6. ==

# 1. > (Greater than operator)
print("Smaller than operator (4 > 2) => "+str(4 > 2)) #True
print("Smaller than operator (1 > 3) => "+str(1 > 3)) #False

# 2. < (Less than operator)
print("Less than operator (5.79 < 7) => "+str(5.79 < 7)) #True
print("Less than operator (3 < 3) => "+str(3 < 3)) #False

# 3. >= (Greater than or equal to operator)
print("Greater than or equal to operator (5 >= 2) => "+str(5 >= 2)) #True
print("Greater than or equal to operator (1 >= 3) => "+str(1 >= 3)) #False
print("Greater than or equal to operator (3 >= 3) => "+str(3 >= 3)) #True

# 4. <= (Less than or equal to operator)
print("Less than or equal to operator (5 <= 9) => "+str(5 <= 9)) #True
print("Less than or equal to operator (7 <= 3) => "+str(7 <= 3)) #False
print("Less than or equal to operator (3 <= 3) => "+str(3 <= 3)) #True

# 5. != (Not equal to operator)
print("Not equal to operator (5!=6) => "+str(5!=6)) #True
print("Not equal to operator (5!=5) => "+str(5!=5)) #False
print("Not equal to operator (hello!=world) => "+str("hello"!="world")) #True

# 6. == (Equal to operator) [= is used for assignment whereas == is used for comparison]
print("Equal to operator (5==5) => "+str(5==5)) #True
print("Equal to operator (5==6) => "+str(5==6)) #False
print("Equal to operator (hello==hello) => "+str("hello"=="hello")) #True
print("Equal to operator (hello==Hello) => "+str("hello"=="Hello")) #Flase - Operators are Case Sensitive

print("Greater than or equal to operator (4.0 >= 4) => "+str(4.0 >= 4)) #True
print("Less than or equal to operator (4.0 <= 4) => "+str(4.0 <= 4)) #True
print("Equal to operator (4.0==4) => "+str(4.0==4)) #True

print("======================================================================")

#Boolean Operators : There are 3 types
#1. and
#2. or
#3. not

#1. and operator
# true and true = true
# true and false = false
# false and true = false
# false and false = false

print(4 > 1 and "word" == "word")            # True and True = True
print(8.76 == 8.7600 and 2 != 2)              # True and False = False
print("earth" == "Earth" and 6 <= 3)        # False and False = False
print(10 == 5 and 10 != 5)                       # False and True = False

#2. or operator
# true or true = true
# true or false = true
# false or true = true
# false or false = false

print(4 > 1 or "word" == "word")       # True or True = True
print(8.76 == 8.7600 or 2 != 2)         # True or False = True
print("earth" == "Earth" or 6 <= 3)   # False or False = False
print(10 == 5 or 10 != 5)                  # False or True = True

#3. not operator
#not True = False
#not False = True

print(not 6482 > 555)   #not True = False
print(not 4==5)           #not False = True

print("======================================================================")

