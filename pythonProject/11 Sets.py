# A set is a data type that consists of a collection of items, much like a list.
# However, sets differ from lists in two important ways.
# 1. The first is that they cannot have duplicate values in them,and
# 2. The second is that the items they contain are unordered like the key-value pairs of a dictionary.

set_1={9,8,8,8,7,6} # if there are duplicate items in a set, then they will be ignored and will only appear once in the set.
set_2= set ({"a","b","c","d","e","a","a"}) # if there are duplicate items in a set, then they will be ignored and will only appear once in the set.
print(set_1) #{8, 9, 6, 7} ->Not in order
print(set_2) #{'d', 'c', 'a', 'e', 'b'} ->Not in order

# Additionally, if you want to create an empty set that you can change later,
# you have to use the set function to create an empty set since just using an
# empty set of curly brackets creates a dictionary instead of a set.

set_3 = set(range(1,12,2))
print(set_3) #{1, 3, 5, 7, 9, 11} ->Not in order

set_4 = {"a", 3.14, 18, True}
print(set_4) #{'a', 18, 3.14, True} ->Not in order

set_5 = {3,6,9,12,15} #sets cannot have their items accessed from them by index.
for num in set_5:
    print(num)

print(12 in set_5)
print(10 not in set_5)
print("-------------------------------------------------------------------------------------------------------------------")

#When are sets in useful?
# Ans-Sets are useful in situations# where you want to use a collection of items but you don't want duplicate items in the collection,
# and you also don't care about the order of the items that make up the collection.

olympic_cities =["Athens", "Paris", "St. Louis", "London", "Stockholm", "Berlin", "Antwerp", "Chamonix", "Paris", "St. Moritz",
                         "Amsterdam", "Lake Placid", "Garmisch-Partenkirchen", "Berlin", "Sapporo Garmisch-Partenkirchen","Tokyo Helsinki",
                         "Cortina d'Ampezzo", "London", "St. Moritz", "London", "Oslo", "Helsinki", "Cortina d'Ampezzo", "Melbourne Stockholm",
                         "Squaw Valley", "Rome", "Innsbruck", "Tokyo", "Grenoble", "Mexico City", "Sapporo", "Munich", "Innsbruck", "Montreal",
                         "Lake Placid", "Moscow", "Sarajevo", "Los Angeles", "Calgary", "Seoul", "Albertville", "Barcelona", "Lillehammer",
                         "Atlanta", "Nagano", "Sydney", "Salt Lake City", "Athens", "Turin", "Beijing", "Vancouver", "London", "Sochi",
                         "Rio de Jansico", "Pyeongchang", "Tokyo", "Beijing", "Paris", "Milan-Cortina d'Ampezzo", "Los Angeles"]

print(set(olympic_cities))
print(len(olympic_cities))
print(list(set(olympic_cities)))
print(len(list(set(olympic_cities))))
print("-------------------------------------------------------------------------------------------------------")

#set methods - there are 8 different set methods - add, remove, discard, clear, copy, union, intersection and difference
#1. add() - The add method takes an item of any data type as its argument and adds that to the set it is called on.

scifi = {"star trek", "star wars", "halo"}
scifi.add("mass effect")
print(scifi) #{'halo', 'star trek', 'mass effect', 'star wars'}

scifi1 = {"star trek", "star wars", "halo"}
scifi1.add("star wars")
print(scifi1) #{'halo', 'star trek', 'star wars'} - duplicate are not allowed in sets
print("-------------------------------------------------------------------------------------------------------")

#2. remove() - The remove method takes one argument of any data type and removes that item from the set that it is called on.
fruits = {"apple", "orange", "banana", "tomato"}
fruits.remove("banana")
print(fruits) #{'orange', 'apple', 'tomato'}
print("-------------------------------------------------------------------------------------------------------")

#3. discard() - Discard does the same thing as remove and also takes one argument. The difference is that if discard is used
# on a piece of data that is not in a set, it will just do nothing instead of giving back an error message.
fruits1 = {"apple", "orange", "banana", "tomato"}
fruits1.discard("pears") #fruits1.discard("apple") - If you use this - then "apple" will removes form the set because "apple" is present in the given set
print(fruits1) #{'banana', 'orange', 'apple', 'tomato'}
print("-------------------------------------------------------------------------------------------------------")

#4. clear() - The clear method takes no arguments and just gets rid of everything in the set that it is called on.
mountains = {"Everest", "Kilimanjaro", "Fuji"}
print(mountains)
mountains.clear()
print(mountains)
print("-------------------------------------------------------------------------------------------------------")

#5. copy() - The copy method returns a copy of a set that has its own place in memory.
mountains_1 = {"Everest", "Kilimanjaro", "Fuji"}
set_2 = mountains_1.copy()
print(set_2 is mountains_1) #False - It means that the original set are not the same set, although if you print the copy,
print(set_2) #{'Everest', 'Kilimanjaro', 'Fuji'}
print("-------------------------------------------------------------------------------------------------------")

#6. union() - The union method allows you to combine all  the items from two different sets into a single set.
set1={1,2,3,4,5}
set2={6,7,8,9}
set3=set1.union(set2) # set1 | set2
print(set3) #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print("-------------------------------------------------------------------------------------------------------")

#7. intersection() - which allows you to find out what items two sets have in common
set4={1,2,3,4,5,7,6,9}
set5={6,7,8,9,3,1,5}
set6=set4.intersection(set5) # set4 & set5
print(set6) #{1, 3, 5, 6, 7, 9}
print("-------------------------------------------------------------------------------------------------------")

#8. subtraction and difference() - you can subtract one set from another based on the items that make up their intersection,
# or in other words, what they have in common.
set11={1,2,3,4,5,9,6}
set12={6,7,8,9,10,2,5}
set13 = set11.difference(set12)  #set11 - set12 --> 2,5,6,9 these are common items from both sets
print(set13) # {1, 3, 4} --> As we have checks set11 so it is removed the common items from set11 & rest are prints in console
# {8, 10, 7} --> As we have checks set12 so it is removed the common items from set12 & rest are prints in console
print("-------------------------------------------------------------------------------------------------------")

#set comprehensions- more advanced way to create a set.
comp1={even+2 for even in range(2,11,2)}
print(comp1)

comp2={char.lower() for char in "ALLCAPS"}
print(comp2)
print("-------------------------------------------------------------------------------------------------------")