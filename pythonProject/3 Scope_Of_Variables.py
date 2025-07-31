#Variables created outside the function has global scope
#Variables created within the function has local scope

#The global scope is created when a program is run & is destroyed when the program ends.

#A local scope is created whenever function is called and all the variables created within that function called exist within that local scope,
#which is returns after something, the local scope of the function called is destroyed and the local variables within it are forgotten.

# Why is understanding variable scope important?
# 1. Local variables cannot be used by code in the global scope.
# 2. Global variables can be accessed by code in a local scope.
# 3. The local scope of one function can 't use variables from another function's local scope.
# 4. You can use the same name for different variables as long as they are in different scopes.

example="this is a global variable" # global scope

def loc_ex():
    example="this is a local variable" # local scope
    return example

print(example) #this is a global variable
print(loc_ex()) #this is a local variable

#-----------------------------------------------------------------------------------------------------------------------

# 1. Local variables cannot be used by code in the global scope.
def loc1():
    breakfast = "Waffles"
    return breakfast

print("Rule1 : "+loc1())
# print(breakfast) # error - name 'breakfast' is not defined

#-----------------------------------------------------------------------------------------------------------------------

# 2. Global variables can be accessed by code in a local scope.
def loc2():
    print(glob_var)

glob_var="Rule2 : This is global variable"
loc2() #Rule2 : This is global variable ------------------------

def var_loc_glob():
    loc_var1="This is local variable + "
    print("Rule2 : "+loc_var1+glob_var1)

glob_var1="This is global variable"
var_loc_glob()

#-----------------------------------------------------------------------------------------------------------------------

# 3. The local scope of one function can 't use variables from another function's local scope

def first():
    low=2
    return low

# def second():
#     return low

print("Rule3 : "+ str(first())) #If we want to print the variable contains integer value & we want to concatenate with string : str(first())
# print(second())

#-----------------------------------------------------------------------------------------------------------------------

# 4. You can use the same name for different variables as long as they are in different scopes.

def loc_ex1():
    fruit = "Apple"
    print("Rule4 : "+fruit)

def loc_ex2():
    fruit = "Banana"
    print("Rule4 : "+fruit)

fruit = "Pineapple"
loc_ex1() #Rule4 : Apple
loc_ex2() #Rule4 : Banana
print("Rule4 : "+fruit) #Rule4 : Pineapple

#-----------------------------------------------------------------------------------------------------------------------

#Gloabl Statement

def local_fun():
    global  car #Car global variable holds the string Tata currently & if we want update with local variable hold Maruti
    car = "Maruti"
    return car

car = "Tata"
print("Global Statement = "+local_fun())
print("Global Statement = "+car)

#-----------------------------------------------------------------------------------------------------------------------

