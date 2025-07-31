#List - It is data type which contains multiple values in an order sequence, values within a list called items
ex_list1=[5, 4, 3, 2, 1]
ex_list2=[2.187,3,987]
ex_list3=["blue", "green", "red", "yellow", "purple", "orange"]
ex_list4=[True, False, False, True, False, True, True, False, True]
ex_list5=[[1, 2, 3],[4, 6],[5, 7, 8, 9]] # list of list
ex_list6=[10, 3.14, "tree", False, [1, 2, 3]] # items in the list, don't need to be of the same data type

print(list("blah")) #['b', 'l', 'a', 'h']

check_list=[1, 2, 3, 4, 5]
print(1 in check_list) #True - basically it checks 1 is available in the list or not, if yes/no it will return the boolean value
not_in_example= 7 not in check_list
print(not_in_example) #True - basically it checks 7 should not available in the list, if yes/no it will return the boolean value
print("---------------------------------------------------------------------------------------")

#Assignment 1
# Do all of this in a .py file in Pycharm.
# Create a variable and assign it a list that contains an integer, a float, a Boolean value, a string, and a list of 3 integers.
# Create another variable and assign it a call of the list() function with a string as its argument.
# Use the keyword "in" to check if the letter "e" is in the list assigned to the variable from step 2 and print the result.
# Use the keyword "not in" to check if the letter "a" is not in the list assigned to the variable from step 2 and print the result.

assign_list1=[10, 3.14, "tree", False, [1, 2, 3]]
assign_list2=list("Tredence")
print("e" in assign_list2)
print("a" not in assign_list2)
print("---------------------------------------------------------------------------------------")

#indexes and list slicing accessing by index -

index_ex=["Rahul", "Ishwar", "Abhijeet"]
print(index_ex[1]) #Ishwar
print(index_ex[1][0]) #I

index_ex1=[[1, 2, 3],[4, 6],[5, 7, 8, 9]]
print(index_ex1[2][1]) #7
print("---------------------------------------------------------------------------------------")

#Negative indexes

negative=[1, 2, 3, 4, 5]
print(negative[-1])
print(negative[-2])
print(negative[-3])
print(negative[-4])
print(negative[-5])
print("---------------------------------------------------------------------------------------")

#using items accessed by index in expressions

mixed=[False, 365, 4.24, "this is a string"]
print(mixed[2]+1.76)
print("I have use \""+mixed[-1]+"\" as an example too many time")
print("---------------------------------------------------------------------------------------")

#list slicing
           #[0,1,2,3,4,5,6,7,8] - indexes
sliced = [1,2,3,4,5,6,7,8,9]
print(sliced[3:])
print(sliced[1:6])
print(sliced[:5])
print("---------------------------------------------------------------------------------------")

#reassigning the list items

reassign = [2,4,6,8,0]
print(reassign)
reassign[3]=10  #replace the item of 3rd index in existence list with 10
print(reassign)
reassign[1:4]=[3,2,1] #replace the item of from 1st to 3rd index in existence list
print(reassign)
reassign[4:7]=[10,100,1000] #replace & add the item of from 4th to 7th index in existence list
print(reassign)
print("---------------------------------------------------------------------------------------")

#Assignment 1
# Do all of this in a .py file in Pycharm.
# Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
# Access the first list from the list of lists in step 1 by index then print it.
# Access the 14 from the list in step 1 then print it.
# Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
# Use a negative integer to access "chair" from the variable in step 4 by index then print it.
# Print "Most people own at least 2 chairs." by concatenating the 2 from the list in step 1 and
# the "chair" from the list in step 4 with "Most people own at least ", a space, and a period.
# Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
# Print the slice [8.76, 6.54, 4.32] from the variable you created in step 7.
# Print the slice [8.76, 6.54] from the variable you created in step 7.
# Print the slice [0.98, 8.76] from the variable you created in step 7.

assign_ex= [[0, 2], [4, 6], [8, 10], [12, 14]]
print(assign_ex[0])
print(assign_ex[3][1])

assign_str=["chair", "table", "desk", "lamp", "bed"]
print(assign_str[-5])
print("\"Most people own at least " + str(assign_ex[0][1]) +" "+ str(assign_str[-5])+"s\"")

assign_float = [0.98, 8.76, 6.54, 4.32]
print(assign_float[1:])
print(assign_float[1:3])
print(assign_float[:2])
print("---------------------------------------------------------------------------------------")

#del and list methods

#del - del statement allows you to delete the values from the list
planets = ["pluto", "mars", "earth", "venus"]
print(planets)
del planets[0] # Usage of del statement
print(planets)

#remove() - this method allows you to remove what you pass it as an argument from the list
planets1 = ["pluto", "mars", "earth", "venus"]
print(planets1)
planets1.remove("pluto") # Usage of remove method
print(planets1)

colors = ["blue", "orange", "blue", "yellow", "red", "blue", "purple"]
print(colors)
colors.remove("blue") # it removes only 1st blue instances out of 3
print(colors)

# Important Note - del statement & remove() method both having same working only the difference is
# del statement deleted the items based on index, while remove() method removes the item based on its argument

# append() method - takes an argument and add item into the list
planet= ["pluto", "mars", "earth", "venus"]
print(planet)
planet.append("neptune") # added the item in the list on last index
print(planet)

#insert() method - It is similar to append(), only the difference is insert allows you to add an item anywhere in the list rather than just at it end
# insert takes 2 arguments => 1st argument is index and 2nd argument is which item will be added in the list

pets = ["parrots","dog","cat"]
print(pets)
pets.insert(2,"tiger") # tiger will add in the list at 2nd index in the list
print(pets)

#sort() - sort the list which is made up of items that are all numbers or strings

num_list = [2.789, 4, -19, 1000, 0]
print(num_list)
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)

str_list = ["rahul", "ishwar", "swapnil", "abhijeet"]
print(str_list)
str_list.sort()
print(str_list)
str_list.sort(reverse=True)
print(str_list)

# Very Important - sort() method cannot be used on mixed lists, which is made up of different types of data in it- because it is not able to differentiate between the data
# only 1 exception for above statement - Python is treated boolean value False=0 & True=1
# so can conclude that if the list contains - numbers, float values & boolean values in it, we can use the sort() method for that list

mixed_data= [44,99,11,3.47,True,12.15,False,1000,-3]
print(mixed_data)
mixed_data.sort()
print(mixed_data)

#Very Important - Sort() method doesn't actually use alphabetical order, but instead it use ASCIIbetical order
# alphabetical order & ASCIIbetical order - both are same except one difference which is - ASCIIbetical order uppercase letters come before the lowercase letters

ASCIIbetical=["Andy", "kiwi", "apple", "Karen", "Brain", "banana"]
print(ASCIIbetical)
ASCIIbetical.sort(key=str.lower) # Due to this list is sort by considering all alphabets are in lowercase
print(ASCIIbetical)
ASCIIbetical.sort() #list is sort by ASCIIbetical order
print(ASCIIbetical)

#index() method -  allows you to find out the index number of an item you pass it as argument
#Importent- remove, append, insert and  sort - It returns the non data type just like a print

metals=["copper","gold","silver","iron"]
print(metals.index("silver"))

numbers=[3,2,1,0,1,2,3]
print(numbers.index(2)) #it will only show index number of 1st time that the item appears in that list will be returned.

#pop() method- It removes and return an item from the list - you can use it instead of del or remove, if you want removed item to return.

companies= ["moto", "mi", "realme", "nokia", "apple"]
print(companies)
end = companies.pop() # last item from the list will remove and stored in the end variable
print(companies)
print(end)

companies1= ["moto", "mi", "realme", "nokia", "apple"]
print(companies1)
end1 = companies1.pop(3) # on 3rd index item from the list will remove and stored in the end variable
print(companies1)
print(end1)
print("---------------------------------------------------------------------------------------")

#Assignment
# Do all of this in a .py file in Pycharm.
# Create a variable called arctic_animals and assign it the list ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
# Use del to remove "tiger" from the list assigned to arctic_animals.
# Use the .remove() method to remove the string "elephant" from the list assigned to arctic_animals.
# Use the .append() method to add the string "arctic fox" to the list arctic_animals.
# Use .insert() to insert the string "snowy owl" between the strings "polar bear" and "walrus" inside of arctic_animals.
# Use the .sort() method to rearrange the strings in arctic_animals into alphabetical order.
# Use print() to display the list assigned to arctic_animals
# Use .index() to get the index number of "reindeer" from arctic_animals then print it.
# Use .pop() to get the last item from the list arctic_animals then print it.

arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
print(arctic_animals)
arctic_animals.remove("elephant")
print(arctic_animals)
arctic_animals.append("arctic fox")
print(arctic_animals)
arctic_animals.insert(2,"snowy owl")
print(arctic_animals)
arctic_animals.sort()
print(arctic_animals)
print(arctic_animals.index("reindeer"))
end2 = arctic_animals.pop()
print(arctic_animals)
print(end2)
print("---------------------------------------------------------------------------------------")

#List Vs String - Both contains order sequence of item,
#In addition, several things that can be done with strings can also be done with lists. Because both of them have index numbers corresponding to what they contain,
# you can access their contents by index, get slices from them, use the length function to get the number of characters or items that they contain,
# and you can even iterate through either of them using a for loop or a while loop.
# The important distinction between lists and strings is that lists are mutable while strings are immutable.

#lists = mutable => means that it can have values be changed,removed, or added.
#strings = immutable => means that it cannot be changed in any way

ex_1=[1,2,3]
print(ex_1)
ex_1[1]=5
print(ex_1)

ex_2="123"
print(ex_2)
ex_2="153" # but re-assigning is possible in the case of string
# ex_2[1]=5 # not possible in the case of string because strings = immutable (Unchangeable)
print(ex_2)

ex_3="No, you can't"
ex_4="Yes"+ex_3[3:11]+"!"
print(ex_4)

ex_5 = 3.14
ex_6 = "coconut"
ex_7 = ex_5
ex_8 = ex_6
print(ex_7)
print(ex_8)

ex_9 = [1,2,3,4,5,6,7,8,9]
ex_10 = ex_9
ex_10[2]=9 #Here I have replaced the 2nd index value with 9 & also applicable for ex_9
print(ex_9) #[1, 2, 9, 4, 5, 6, 7, 8, 9] --> You can see that 2nd index value is also updated for ex_9 variable
print(ex_10) #[1, 2, 9, 4, 5, 6, 7, 8, 9]

#Rule to remember - mutable(changeable-list) & immutable(unchangeable- integers, floats, strings, and Boolean values)
# All mutable data types are stored as references,and all immutable data types are actually stored as themselves.
# This means that immutable data types like integers, floats, strings, and Boolean values don't have the reference problem
# that can occur when working with mutable data types like lists.
print("---------------------------------------------------------------------------------------")

#copy module & deepcopy() function
import copy
ex_12 =[1,2,3,4,5]
print(ex_12)

ex_13 = copy.deepcopy(ex_12) #This method creates a copy of the ex_12 list and assigns it to ex_13, so changes to ex_13 do not affect ex_12.
ex_13[2]=4 #Here I have replaced the 2nd index value with 4 & this applicable only for the ex_13 variable & not for ex_12, its only because of copy module & its deepcopy function
print(ex_12)
print(ex_13)

ex_14 = ex_13
ex_14[4] = 6 #Here I have replaced the 4th index value with 6 & also applicable for ex_13
print(ex_13)
print(ex_14)

# Usually Python uses four space indents to be able to tell what code belongs to what.
# For example, if an else statements and functions have code within them that needs to be indented for Python to know
# that code is associated with them. However, it is a bit different with lists. Lists can span multiple lines.
# This is useful for longer lists with many items where you don't want all the items on the same very long line of code.
# Despite all the space before the strings, "fern", "tree", and "moss" in this example, Python knows that all three are not separate lines of code
# because of the brackets enclosing them

ex_15 = ["bush",
                "fern",
                "tree",
                "moss"]
print(ex_15)

#For things other than lists that you want to span multiple lines,
# you can use the line continuation character which is a backslash.

ex_16 = (2 +\
              4 +\
              6)
print(ex_16)

#When you use the line continuation character inside of strings, do not try to line everything up
# like you would with a math expression by adding spaces. Doing so will add more spaces
# to the string being made to span multiple lines.

ex_17 = "The emp\
ire strikes\
 back"
print(ex_17)

#If you are using the line continuation character on a concatenated string,
# you should line everything up vertically like you would with a math expression.

ex_18 = "Hello " + \
             "world"
print(ex_18)
print("---------------------------------------------------------------------------------------")

# Find out the common items from the 2 lists
list1 = [1,2,3,4,5,6]
list2 = [5,6,7,8,9]
for i in list1:
   if i in list2:
        print("Common items from list1 & list2 lists ---> "+str(i))

print("---------------------------------------------------------------------------------------")

