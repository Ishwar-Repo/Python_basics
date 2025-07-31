#  Tuples are a data type made up of a collection of items. While they are similar to lists in that regard, they differ from lists in a few ways.
#  The first is that they are enclosed in parentheses instead of square brackets.
# When we create a tuples then - The tuple function returns the tuple and takes one argument that must be of an iterable data type. That argument should be a list or string.
# Unlike lists and dictionaries, tuples are an immutable data type, which means that they cannot be changed.
#Tuples are useful for when you want to have a collection of data that you know you will not change later on in the program.

tuple_1 = ("a", "b", "c", "d", "e") #can all be of the same data type, such as the strings
tuple_2 = (3.789, False, [1, 2, 3]) #they can be of different data types,
tuple_3 = (1, 1, 0, 0, 0) # the same item within a tuple, such as the two instances of one and the three instances of zero

tuple_4 = tuple([3.14, 2.205, 10]) #List -
tuple_5 = tuple("edcba") #String
print(tuple_4)
print(tuple_5)

tuple_6 = tuple({"a":1, "b":2, "c":3}) #dictionary
print(tuple_6)

tuple_7 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) #you can also access values from a tuple by index or by slice, like you can with lists or strings.
print(tuple_7[2]) # 3
print(tuple_7[:8]) # (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple_7[2:7]) # (3, 4, 5, 6, 7)
print(tuple_7[3:]) # (4, 5, 6, 7, 8, 9, 10)

# Tuples are useful for when you want to have a collection of data, that you know you will not change later on in the program.
# This is because their inability to be changed will prevent unwanted changes from being made to them.

tuple_8 = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
tuple_9 = ("Summer", "Winter", "Rainy")
tuple_10 = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
                   "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

# Another reason to use tuples over lists, is that they take up less space in memory.
# hence we can conclude that tuples are faster than the list because it less space utilization
tuple_11 = (1, 2, 3)
list1 = [1, 2, 3]
print(tuple_11.__sizeof__()) #48 bytes
print(list1.__sizeof__()) #72 bytes

occupations = {("Angus", "Young"): "musician",
                        ("Narendra", "Modi"): "prime minister",
                        ("Richard", "Branson"): "entrepreneur",
                        ("Quentin", "Tarantino"): "filmmaker"}

seven_wonders = {("29°58′44″N", "31°08′02″E"): "The Great Pyramid of Giza, Egypt",
                              ("33°13′23″N", "43°40′45″E"): "Hanging Gardens of Babylon",
                              ("37°38′18″N", "21°37′47″Е"): "Archaeological Site of Olympia, Greece",
                              ("37°55′33″N", "23°59′36″E"): "Temple of Artemis at Ephesus",
                              ("37°02′16″N", "27°25′26″E"): "Mausoleum at Halicarnassus",
                              ("36°26′02″N", "28°13′03″E"): "Rhodes, Greece",
                              ("31°12′51″N", "29°53′28″E"): "Lighthouse of Alexandria, Egypt"}

print("-------------------------------------------------------------------------------------------------------------------")

# Tuple looping & steps

major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")
for city in major_cities:
    print(city)
print()

major_cities2 = ("Tokyo", "London", "New York", "Shanghai", "Sydney")
count = 0
while count < len(major_cities2):
    print(major_cities2[count])
    count+=1
print()

major_cities3 = ("Tokyo", "London", "New York", "Shanghai", "Sydney")
backward = len(major_cities3) - 1
while backward >= 0:
    print(major_cities3[backward])
    backward-=1
print()

major_cities4 = ("Tokyo", "London", "New York", "Shanghai", "Sydney")
print(major_cities4[4::-1])

print("-------------------------------------------------------------------------------------------------------------------")

#tuples slicing with step - Very Important

ints = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(ints[::3]) #(1, 4, 7, 10) - Stride length of 3
print(ints[1::2]) #(2, 4, 6, 8, 10) - evens only
print(ints[7::-1]) #(8, 7, 6, 5, 4, 3, 2, 1) - backward from 8
print(ints[8::-2]) # (9, 7, 5, 3, 1) - odds only backwards
print("-------------------------------------------------------------------------------------------------------------------")

#tuple methods:

nested = (1,2,3, (4,5,6), (7,8,9), (10,11,12))
print(nested[4])
print(nested[5][1])
print("-------------------------------------------------------------------------------------------------------------------")

# count() method - It basically counts the repeated items from tuples
repeat = (7,3,3,0,0,7,0,0)
print(repeat.count(7))
print(repeat.count(3))
print(repeat.count(0))
print("-------------------------------------------------------------------------------------------------------------------")

# index() method - If you know a value exists in a tuple, but you don't know its index number.
# If you use the index method on a tuple that has multiple instances of the same value,
# then the index number of the first time that that value appears in the tuple will be returned.
ints = (1,1,7)
print(ints.index(7))
print(ints.index(1))

print("-------------------------------------------------------------------------------------------------------------------")


