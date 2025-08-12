# Dictionaries are a data type which can store a collection of values like a list.
# A dictionary is different from a list in that instead of having to have each of its items
# be assigned to an index number that is an integer, the items that a dictionary contains are assigned to keys
# which can be different data types such as floats and strings.

# To create a dictionary, you start by typing curly brackets.

console = {"microsoft": "exel", "lenovo": "mouse", "folder": "files"}
#You can use keys to access values from a dictionary like you would use index numbers to access the items in a list or the characters in a string.
print(console["lenovo"])
val = console["lenovo"]
print(val)
print("The Ai related "+console["folder"]+" are stored in your computers")

moh_hardness ={9:"corundum", 10:"diamond"} #The keys in this dictionary are integers.
floats = {1.23:100, 3.14:1000, 2.718:10000} #The keys in this  dictionary are all floats,
mixed = {"string":1, 10210:2, 4.987:3, True:4} #and keys in this dictionary has keys of varying data types.

#dictionaries are unordered - Very Important
print([1,2,3]==[1,2,3]) #Lists need to have the exact same items in the exact same order ->True
print([4,5,6]==[6,5,4]) #both lists contain the same items, the items are not in the same order within the list. -> False

first = {0:2.1, 1:2.2, 2:2.3, 3:2.4, 4:2.5}
second = {4:2.5, 2:2.3, 1:2.2, 3:2.4, 0:2.1}
print(first==second) #Two dictionaries being compared both need to contain the same key & value pairs for them to be considered equal.

first = {0:2.1, 1:2.2, 2:2.3, 3:2.4, 4:2.5}
print(0 in first)
print(1 not in first)

#Assignment 1 - Do all of this in a .py file in Pycharm.
# create a variable and assign it a dictionary that has 5 key value pairs
# print and access the value held at the third key in the dictionary
# use the in keyword to check if a key appears in the dictionary and print the result
# use not in to check if a key does not appear in the dictionary and print the result

assignment = {1:11.11, 2:22.22, 3:33.33, 4:44.44, 5:55.55}
print(assignment[3])
print(1 in assignment)
print(7 not in assignment)
print("---------------------------------------------------------------------------------------")

#Dictionary Methods 1 : keys(), values(), items() and get()
#1. keys() method -
birth_yrs = {1992:"ishwar", 1996:"dimpal", 1995:"vijay", 1966:"pappa", 1976:"mummy"}
print(birth_yrs.keys()) #Use of key() method
for key in birth_yrs.keys():
    print(key)
print("---------------------------------------------------------------------------------------")

#2. values() method -
print(birth_yrs.values()) #Use of value() method
for values in birth_yrs.values():
    print(values)
print("---------------------------------------------------------------------------------------")

#3. items() method -
print(birth_yrs.items()) #Use of items() method
for key, value in birth_yrs.items():
    print(key, value)

print(type(birth_yrs.keys()))
print(type(birth_yrs.values()))
print(type(birth_yrs.items()))

print(list(birth_yrs.keys())) #[1992, 1996, 1995, 1966, 1976]
print(list(birth_yrs.values())) #['ishwar', 'dimpal', 'vijay', 'pappa', 'mummy']
print(list(birth_yrs.items())) #[(1992, 'ishwar'), (1996, 'dimpal'), (1995, 'vijay'), (1966, 'pappa'), (1976, 'mummy')] -->tuple
print("---------------------------------------------------------------------------------------")

#Using in and not in on values
print("dimpal" in birth_yrs.values())

#get() method
birth_yrs1 = {1991:"ishwar", 1995:"dimpal", 1994:"vijay"}
if 1975 in birth_yrs1:
    print(birth_yrs1[1975])
else:
    print("1975 key is not a part of birth_yrs dictionary")

#OR - Use of get() method below

print(birth_yrs.get(1975, "1975 key is not a part of birth_yrs dictionary"))
print("---------------------------------------------------------------------------------------")

#Other things you should know about the dictionaries
edu_yrs = {2007:"10th",
                  2009:"12th",
                  2013:"BE"
                  }
print(edu_yrs)
education = edu_yrs #assigned a dictionary,it is actually a reference to a dictionary that is being stored not an actual dictionary.
education[2013]="ME"
print(edu_yrs)

print(len(edu_yrs))
print("---------------------------------------------------------------------------------------")

#Assignment 1-Do all of this in a .py file in Pycharm.
# create a variable and assign it the following dictionary:
# {"Queen": "Bohemian Rhapsody", "Bee Gees": "Stayin' Alive", "U2": "One", "Michael Jackson": "Billie Jean", "The Beatles": "Hey Jude", "Bob Dylan": "Like A Rolling Stone"}
# make the dictionary span multiple lines so that the line the dictionary starts on is not too long.
# print the length of the dictionary.
# use the .keys() method and a for loop to get and print all  the keys from the dictionary on separate lines.
# print all the values from the dictionary using the .values() method.
# use .items() with a for loop to iterate through and print all the key value pairs from the dictionary.
# use the .get() method to check the dictionary for the key"Promise of the Real"
# and create a message that will print if the key is not found in the dictionary.

assg_dic={
            "Queen": "Bohemian Rhapsody",
            "Bee Gees": "Stayin' Alive",
            "U2": "One",
            "Michael Jackson": "Billie Jean",
            "The Beatles": "Hey Jude",
            "Bob Dylan": "Like A Rolling Stone"
            }
print(len(assg_dic))
print(assg_dic.keys())
for keys in assg_dic.keys():
    print(keys)
print(assg_dic.values())
for keys, values in assg_dic.items():
    print(keys,values)

print(assg_dic.get("Promise of the Real", "\"Promise of the Real\""" this key is not available in assg_dic dictionary"))
print("---------------------------------------------------------------------------------------")
#Dictionary Methods 3 : fromkeys(), pop() and popitem()

#1. fromkeys() method - It returns a dictionary using two values that it was given as arguments.
# The first argument it takes is used as keys and the second argument is used as a value.

exx1={}.fromkeys(["address"],"Maharashtra India")
print(exx1) #{'address': 'Maharashtra India'} --here address is list so it is considered as Key

exx_1={}.fromkeys("add","Maharashtra India")
print(exx_1) #{'a': 'Maharashtra India', 'd': 'Maharashtra India'} -- here each character in the string would become a key & repeated characters are only used once in a key value pair rather than as many times as they appear in an iterable.

exx_11={}.fromkeys(["brand"])
print(exx_11) #{'brand': None}

exx_11={}.fromkeys("brand")
print(exx_11) #{'b': None, 'r': None, 'a': None, 'n': None, 'd': None}
print("---------------------------------------------------------------------------------------")

#2. pop() method - It removes an item, where an item in a dictionary is a key value pair.
#However, it is a bit of a different situation for dictionaries since you can't just call .pop() on a dictionary
# with no argument, and then have it remove the last key value pair. This is due to the fact that dictionaries are unordered.

exx2={"make":"Honda", "model":"civic", "year":2016}
print(exx2) # {'make': 'Honda', 'model': 'civic', 'year': 2016}
pop_method=exx2.pop("model")
print(exx2) # {'make': 'Honda', 'year': 2016}
print(pop_method) #civic
print("---------------------------------------------------------------------------------------")

#3. popitem() method - It allows you to remove the last key value pair, from a dictionary without having to give it an argument.

exx3={"name":"bob", "age":38, "occupation":"accountant","workPlace":"HR Block"}
pop_items = exx3.popitem()
print(exx3) #{'name': 'bob', 'age': 38, 'occupation': 'accountant'}
print(pop_items) #('workPlace', 'HR Block')
print("---------------------------------------------------------------------------------------")

# Assignment - Do all of this in a .py file in Pycharm.
# use .fromkeys() to create a dictionary that has the consonants from the alphabet as its keys and the string
# "consonant" as the value for each of those keys.  Only use lower case letters for the consonants.
# "y" counts as a consonant for this exercise.  Use a for loop and the .items() method to print each of
# those key: value pairs on a different line.  For example, the first 3 lines in the output should be the
# following:b consonant c consonant d consonant paste this dictionary into your .py file then pop and
# print "Big Mac" from it fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
# use .popitem() to remove the last key: value pair from the dictionary assigned to fast_food_items then print new fast_food_items dictionary.

assign = {}.fromkeys("bcdfghjklmnpqrstvwxyz","consonant")
for keys, values in assign.items():
    print(keys, values)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
pops = fast_food_items.pop("McDonald's")
print(pops) #Big Mac

fast_food_items1 = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
pops_items = fast_food_items1.popitem()
print(fast_food_items1) #{"McDonald's": 'Big Mac', 'Burger King': 'Whopper'}
print("---------------------------------------------------------------------------------------")

#Dictionary Methods 4 : clear(), copy() and update()

# 1. clear()- It just removes everything from a dictionary that it is called on resulting in an empty dictionary.
#  The .clear method takes no arguments.

exx4={1:"India", 2:"Russia", 3:"China", 4:"Japan", 5:"Thailand"}
print(exx4)
exx4.clear()
print(exx4)
print("---------------------------------------------------------------------------------------")

# 2. copy() - It is assigned a dictionary,it is actually a reference to a dictionary that is being stored not an actual dictionary.
birth_yrs1 = {1992:"ishwar", 1996:"dimpal", 1995:"vijay", 1966:"pappa", 1976:"mummy"}
print(birth_yrs1) #{1992: 'ishwar', 1996: 'dimpal', 1995: 'vijay', 1966: 'pappa', 1976: 'mummy'}
people=birth_yrs1.copy() #This method creates a copy of the "birth_yrs1" dictionary and assigns it to "people", so changes to "people" do not affect "birth_yrs1".
people[1996]="rani"
print(birth_yrs1) #{1992: 'ishwar', 1996: 'dimpal', 1995: 'vijay', 1966: 'pappa', 1976: 'mummy'}
print(people) #{1992: 'ishwar', 1996: 'rani', 1995: 'vijay', 1966: 'pappa', 1976: 'mummy'}
print("---------------------------------------------------------------------------------------")

#3. update()- It allows us to add key-value pairs from one dictionary to another or overwrite the values of existing keys in a dictionary with values from another dictionary.
# this method takes one argument
city_info = {"country":"Canada", "province":"Ontario", "city":"Toronto"}
population_1 = {"populations":293000}
city_info.update(population_1)
print(city_info) #{'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'populations': 293000}
print(population_1) #{'populations': 293000}

city_info1 = {"country":"Canada", "province":"Ontario", "city":"Toronto"}
populations1= {"populations":293000}
city_info1.update(populations1)
print(city_info1)#{'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'populations': 293000}
city_info1["populations1"]=300000
print(city_info1) #{'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'populations': 293000, 'populations1': 300000}
city_info1.update(populations1)
print(city_info1) #{'country': 'Canada', 'province': 'Ontario', 'city': 'Toronto', 'populations1': 300000, 'populations': 293000}
print("---------------------------------------------------------------------------------------")

#Assignment 1 - Do all of this in a .py file in Pycharm. paste these 2 dictionaries into your file
# internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
# another_one = {"shroud": "Twitch"}
# use .update() to add the contents of another_one to internet_celebrities.
# create a variable and assign it a copy of internet_celebrities.
# use the .clear() method to get rid of the contents of internet celebrities. print internet_celebrities.
# print the variable you created in step 3.

internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)
ass_var = internet_celebrities.copy()
internet_celebrities.clear()
print(internet_celebrities) #{}
print(ass_var) #{'DrDisrespect': 'YouTube', 'ZLaner': 'Facebook', 'Ninja': 'Mixer', 'shroud': 'Twitch'}
print("---------------------------------------------------------------------------------------")

#Dictionary Methods 4 : setdefault() method -

computers = {"google":"chromebook", "apple":"macbook", "microsoft":"surface Pro"}
print(computers) #{'google': 'chromebook', 'apple': 'macbook', 'microsoft': 'surface Pro'}
if "Lenovo" not in computers:
    computers["Lenovo"]="ThinkPad"
print(computers) #{'google': 'chromebook', 'apple': 'macbook', 'microsoft': 'surface Pro', 'Lenovo': 'ThinkPad'}

computers1 = {"google":"chromebook", "apple":"macbook", "microsoft":"surface Pro"}
print(computers1) #{'google': 'chromebook', 'apple': 'macbook', 'microsoft': 'surface Pro'}
computers1.setdefault("Lenovo","ThinkPad") #If the specified key already exists in the dictionary, this method cannot be overridden to update its value
print(computers1) #{'google': 'chromebook', 'apple': 'macbook', 'microsoft': 'surface Pro', 'Lenovo': 'ThinkPad'}
computers1.setdefault("Lenovo","IdeaPad")
print(computers1) #{'google': 'chromebook', 'apple': 'macbook', 'microsoft': 'surface Pro', 'Lenovo': 'ThinkPad'}

computers2 = {"google":"chromebook", "apple":"macbook", "microsoft":"surface Pro"}
print(computers2) #{'google': 'chromebook', 'apple': 'macbook', 'microsoft': 'surface Pro'}
computers2.setdefault("apple","macbook pro") #If the specified key already exists in the dictionary, this method cannot be overridden to update its value
print(computers2) #{'google': 'chromebook', 'apple': 'macbook', 'microsoft': 'surface Pro', 'Lenovo': 'ThinkPad'}

#If the specified key already exists in the dictionary, this method cannot be overridden to update its value, (You can refer above example)
#as you can see that we tried to update value of "Lenovo" key with "IdeaPad" but in o/p it is showing only 'Lenovo': 'ThinkPad'
print("---------------------------------------------------------------------------------------")

# dict() function - alternate to create dictionary in python
# created using the dict function key-value pairs, then for each key-value pair type, the key equals then the value in the parentheses of dict().
# When you do this, there should be no spaces on either side of the equals sign.

empty = dict()
print(empty) #{}
with_value = dict(a1=1,b_=2, c_3=3)
print(with_value) #{'a': 1, 'b': 2, 'c': 3}

#  a dict() function call can't contain punctuation, special characters such as dollar symbols, semicolons or asterisks, and they can't be Boolean values.
# when using the dict() function, the first character of the key cannot be a number.
print("---------------------------------------------------------------------------------------")

