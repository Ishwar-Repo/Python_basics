# String Part II

#1. Convert string from lowercase to upper case or vice versa using methods .upper() and .lower()
all_lower = "here only lower case alphabets written"
print(all_lower)
print("String is converted into upper case => "+str(all_lower.upper()))
print("---------------------------------------------------------")

all_upper = "HERE ONLY UPPER CASE ALPHABETS WRITTEN"
print(all_upper)
print("String is converted into lower case => "+str(all_upper.lower()))
print("---------------------------------------------------------")

title_case= "tredence analytical solutions pvt ltd"
print("I =>"+str(title_case).title()) #title() - It converts the 1st alphabets to upper case of each word , if it is in lower case

#2. Checking is variable contains lower or upper case & returns the boolean value using methods
#.isupper() - It returns true when all alphabets (interested in alphabets only) are in upper case, if not then it returns False
# and .islower() - It returns true when all alphabets (interested in alphabets only) are in lower case , if not it returns False

lower_case="ishwar"
print("1 "+str("ishwar".islower())) #True
print("2 "+str(lower_case.islower())) #True
print("3 "+str(lower_case.isupper())) #False
print("---------------------------------------------------------")

upper_case="ISHWAR"
print("4 "+str("$100 ISHWAR".isupper())) #True
print("5 "+str("$100 ishwar".islower())) #True
print("6 "+str("!@#$%^&*".islower())) #False
print("7 "+str("37&8.,:\"".islower())) #False
print("8 "+str(upper_case.islower())) #False
print("9 "+str(upper_case.isupper())) #True
print("---------------------------------------------------------")

#Multiple String Methods:
print("10 "+str("Shout!".lower().isupper()))

#isalpha() - Only returns Letters
#isalnum() - Only returns Numbers And Letters
#isdecimal() - Only returns Numbers
#isspace() - Only returns Spaces
#istitle() - Only returns Titlecase

print("11 "+str("Batman".isalpha())) #True
print("12 "+str("Batman123".isalnum())) #True
print("13 "+str("1214".isdecimal())) #True
print("14 "+str("3.14".isdecimal())) #False
print("15 "+str("    ".isspace())) #True
print("16 "+str("not just spaces"[3].isspace())) #True
print("17 "+str("Ishwar Jagannath Suranje".istitle())) #True - its checks all words 1st letter, it is in upper case then - True
print("18 "+str("Ishwar: Suranje!".istitle())) #True
print("---------------------------------------------------------")

#startswith() and endswith()
print("19 "+str("this is string".startswith("this")))
print("20 "+str("this is string".startswith("t")))
print("21 "+str("this is string".endswith("string")))
print("22 "+str("this is string!".endswith("!")))
print("---------------------------------------------------------")

#join method
print("23 "+str("".join(["one","two","three"])))
print("23 "+str(" ".join(["one","two","three"])))
print("23 "+str(", ".join(["one","two","three"])))
print("23 "+str(",  ".join(["one","two","three"])))
print("23 "+str("...".join(["one","two","three"])))
print("---------------------------------------------------------")

#split method
print("24 "+str("Eggs, Milk, Waffle, bacon".split()))
#by default  - separates word by spaces - after comma spaces are seen - 24 ['Eggs,', 'Milk,', 'Waffle,', 'bacon']

print("24 "+str("Eggs, Milk, Waffle, bacon".split(",")))
#commas are removed, spaces are kept as it is  - 24 ['Eggs', ' Milk', ' Waffle', ' bacon']

print("24 "+str("Eggs, Milk, Waffle, bacon".split(", ")))
#commas nad spaces are removed  - 24 ['Eggs', ' Milk', ' Waffle', ' bacon']
print("---------------------------------------------------------")


#Assignment
# Do all of this in a .py file in Pycharm:
# Create a variable called mixed_case and assign it the string "A Song of Ice and Fire"
# Use .isupper() to check if mixed_case is a string of all upper case letters.  print() the result.
# Use .islower() to check if mixed_case is a string of all lower case letters.  print() the result.
# Change all the letters in mixed_case to upper case letters using .upper() and print() the result.
# Change all the letters in mixed_case to lower case letters using .lower() and print() the result.
# Use the .istitle() method to check if mixed_case is title case and print the result.
# Create a variable called title_case and assign it the result of .title() being called on mixed_case.
# print() title_case
# Call startswith() on mixed_case with the letter mixed_case starts with as its argument.  print() the result.
# Call endswith() on mixed_case with the letter mixed_case ends with as its argument.  print() the result.
# Create a variable called words and assign it the result of split() being used on mixed_case.
# print the variable "words"
# Use the .join() method to join together all the items in the list assigned to words as a single string.
# Use .isalpha() to check if the string is made up entirely of letters.  Finally, use print() to display the result.

mixed_case="A Song of Ice and Fire"
print("Assignment 1=>"+str(mixed_case.isupper()))
print("Assignment 2=>"+str(mixed_case.islower()))
print("Assignment 3=>"+str(mixed_case.upper()))
print("Assignment 4=>"+str(mixed_case.lower()))
print("Assignment 5=>"+str(mixed_case.istitle()))
title_case=mixed_case.title()
print("Assignment 6=>"+str(title_case))
print("Assignment 7=>"+str(mixed_case.startswith("A")))
print("Assignment 8=>"+str(mixed_case.endswith("e")))
words=mixed_case.split()
print("Assignment 9=>"+str(words)) #Very Important - ['A', 'Song', 'of', 'Ice', 'and', 'Fire']
print("Assignment 9=>"+str("".join(words))) #Very Important - ASongofIceandFire
print("Assignment 10=>"+str("".join(words).isalpha())) #Very Important -  True
print("---------------------------------------------------------")

#rjust() and ljust() method - both take one argument and return right justified or left justified versions of the string they are called on

print("rjust() method is used =>"+"hello world".rjust(15)) #string contains 11 char including space, as rjust() method is used, so it's justified right with 4 spaces
print("ljust() method is used =>"+"hello world".ljust(15)+"four spaces later") #string contains 11 char including space, as ljust() method is used, so it's justified left with 4 spaces

print("rjust() method is used with 2nd argument =>"+"hello world".rjust(15,"_")) #string contains 11 char including space, as rjust(IInd argument only "string") method is used, so it's justified right with 4 (_)
print("ljust() method is used with 2nd argument =>"+"hello world".ljust(15,"*")) #string contains 11 char including space, as rjust(IInd argument only "string") method is used, so it's justified right with 4 (*)

#center() method is working in similar manner like rjust() and ljust() methods
print("center() method is used =>"+"hello world".center(15)) #string contains 11 char including space, as center() method is used, so it's justified on both side of string (2 spaces left & 2 spaces right)
print("center() method is used with 2nd argument =>"+"hello world".center(15,"*")) #string contains 11 char including space, as center() method is used, so it's justified on both side of string (2 STAR left & 2 STAR right)
print("center() method is used with 2nd argument =>"+"hello world".center(16,"*")) #string contains 11 char including space, as center() method is used, so it's justified on both side of string (2 STAR left & 2 STAR right)

#strip(), rstrip() and lstrip() methods - arguments for all 3 methods need to be String
#1. strip() - It is used when you want to remove characters such as white spaces, by default strip removes all the spaces from both side of string
#2. rstrip() - It is used when you want to remove all the spaces from the right side of string
#3. lstrip() -  It is used when you want to remove all the spaces from the left side of string

print("I had exciting trip !!!11111")
print("strip() method is used =>"+"1111I had exciting trip !!!11111".strip("1"))
print("strip() method is used =>"+"blueblueyellowblue".strip("eulb")) #Important
print("rstrip() method is used =>"+"1111I had exciting trip !!!11111".rstrip("1"))
print("rstrip() method is used =>"+"juice, bread, cheese, beef, bread".rstrip(", bread"))
print("rstrip() method is used =>"+"juice, bread, cheese, beef, bread".rstrip(",ed arb")) #Important
print("lstrip() method is used =>"+"1111 I had exciting trip !!!11111".lstrip("1"))
print("lstrip() method is used =>"+"juice, bread, cheese, beef, juice".lstrip("juice, "))

#replace() method - Which is used to search for and replace a string (It takes 2 strings as arguments) - 1st string used for search & 2nd string is used for replacement
print("replace() method is used =>"+"Good Morning".replace("Morning","Afternoon"))
print("replace() method is used =>"+"Dimpal Kishor Tijvij".replace("Kishor Tijvij","Ishwar Suranje"))
print("---------------------------------------------------------")

#Assignment -
# Do all of this in a .py file:
# Create a variable called the_string and assign it the string "North Dakota".
# Call .rjust() on the_string with 17 as its argument and print() the result.
# Call .ljust() on the_string with the arguments 17 and "*" then print() the result.
# Create a variable called center_plus and assign it the result of .center() being called on the_string with 16 and "+" as arguments.
# Use print() to display the string assigned to center_plus.
# Call .lstrip() on the_string to remove "North" then print() the result.
# Call .rstrip() on center_plus with "+" as its argument and print() the result.
# Call .strip() on center_plus with "+" as its argument and print() the result.
# Call .replace() on the_string and replace "North" with "South".  print() the result.

the_string="North Dakota"
print("rjust() method is used =>"+str(the_string.rjust(17,)))
print("ljust() method is used =>"+str(the_string.ljust(17,"*")))
center_plus=the_string.center(16,"+")
print("center() method is used =>"+str(center_plus))
print("lstrip() method is used =>"+str(the_string.lstrip("North")))
print("rstrip() method is used =>"+str(center_plus.rstrip("+")))
print("strip() method is used =>"+str(center_plus.strip("+")))
print("replace() method is used =>"+str(center_plus.replace("North","South")))
print("---------------------------------------------------------")

#len() method - you will get the length
print("len() method is used =>"+str(len("tree")))
print("len() method is used =>"+str(len("This"+" "+"is"+" "+"a"+" "+"String")))
print("len() method is used =>"+str(len("This"+" "+"is a"+" "+"String")))
print("string slicing is used =>"+str("antidisestablishmentarianism"[7:20]))
print("len() method is used =>"+str(len("antidisestablishmentarianism"[7:20])))
print("---------------------------------------------------------")

#Assignment 1 -
# For this challenge, you will be writing a program which uses a for loop to reverse a string.
# Start by creating a variable and assigning it a string as user input using input().
# Use a for loop to reverse the string.  You will need to use range with all 3 inputs for this.
# In addition, you should create a variable before the for loop and assign it an empty string.
# The variable will be reassigned multiple times within the for loop and end up holding the new reversed string.
# Print the reversed string at the bottom of your program.

name="Tredence" #T-0,r-1,e-2,d-3,e-4,n-5,c-6,e-7
empty=""
for char in range(len(name) -1,-1,-1):
    empty+=name[char]
print("Reversed of the given string by char =>"+str(empty))

#or
print("Reversed of the given string by char (Using the Slicing of String)=>"+name[::-1])

#and
print("Reversed the string by words =>")
bhavesh="Bhavesh is a james bond".split(" ")
for i in bhavesh[::-1]:
    print(i, end=" ")
print()
print("---------------------------------------------------------")

#Assignment 1 -
# For this programming challenge, write a function in a .py file
# which takes 1 string as an argument, finds out the number of words in that string, then returns that number.
# For example, if the program was used on the string "This is a string.", then the function would return 4.
# Assumptions:
# Assume that the string will be assigned to a variable and that it will contain at least 1 word.
# Assume that there will never be 2 or more consecutive spaces in a row within the string.
# Contractions and possessive words with an apostrophe like "it's" or "Brian's" count as 1 word.
# Hyphenated words like "ice-cream" count as 1 word.
# Numbers in the string such as the "007" in "James Bond is 007." count as words
# There will be no double quotes "" within in the string.
# Hints for this problem:
# Use string methods to filter out characters besides numbers, letters, spaces, apostrophes, and hyphens.
# Count the number of spaces in the filtered string and add 1 to that since the string will always contain at least 1 word.
# This will give you the number of words it contains.
# You should test your program with many different strings.
# However, the strings that the solution code is being used on are the 3 strings below.
# str_1 = "James Bond is 007."
# str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
# str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
# saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
# shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
# shrimp burger, shrimp sandwich. That- that's about it."
# So, for your final solution, copy the above into your .py file and print() 3 calls of your function, once for each of the 3 variables above.

str_1 = "James Bond is 007."
str_2 = "When the moon hits your eye like a big pizza pie, that's amore!"
str_3 = "Anyway, like I was sayin', shrimp is the fruit of the sea. You can barbecue it, boil it, broil it, bake it, \
saute it. Dey's uh, shrimp-kabobs, shrimp creole, shrimp gumbo. Pan fried, deep fried, stir-fried. There's pineapple \
shrimp, lemon shrimp, coconut shrimp, pepper shrimp, shrimp soup, shrimp stew, shrimp salad, shrimp and potatoes, \
shrimp burger, shrimp sandwich. That- that's about it."

def word_counter(words):
    spaces_and_letters = ""
    word_count = 1
    for i in words:
        if i.isalnum() or i.isspace() or i == "-" or i == "'":
            spaces_and_letters += i
    for j in spaces_and_letters:
        if j == " ":
            word_count += 1
    return word_count
print(word_counter(str_1))
print(word_counter(str_2))
print(word_counter(str_3))

#or
print(len(str_1.split(" ")))
print(len(str_2.split(" ")))
print(len(str_3.split(" ")))
print("---------------------------------------------------------")

#format() method -

name="Ishwar"
degree="Software Engineer"
job="Automation Test Engineer"
experience="7 Yrs_+"
print(name+" majorly in "+degree+" works as a "+job+" and he has "+experience+" experience.")
print("{} majorly in {}, works as a {} and he has{}  experience.".format(name,degree,job,experience)) # Important
print("---------------------------------------------------------")
