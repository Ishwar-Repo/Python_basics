bhavesh="Bhavesh is a james bond".split(" ")
print(len(bhavesh))

name="Tredence" #T-0,r-1,e-2,d-3,e-4,n-5,c-6,e-7
                             #T=-8,r=-7,e=-6,d=-5,e=-4,n=-3,c=-2,e=-1
print(name[::-1])

# list -- 1 to 1000 multiple of 13 and divisible by 3
# print(list(range(0,1000,39)))

bhavesh="Bhavesh is a james bond".split(" ")
for i in bhavesh[::-1]:
    print(i)
print()

# Find out the common items from the 2 lists
list1 = [1,2,3,4,5,6]
list2 = [5,6,7,8,9]
for i in list1:
   if i in list2:
        print(i)

import copy
ex_12 =[1,2,3,4,5]
print("this is the output of ex_12 --> "+str(ex_12))

ex_13 = copy.deepcopy(ex_12) #
ex_13[2]=4 #Here I have replaced the 2nd index value with 4 & this applicable only for the ex_13 variable & not for ex_12, its only because of copy module & its deepcopy function
print("this is the output of ex_12 --> "+str(ex_12))
print("this is the output of ex_13 --> "+str(ex_13))

ex_14 = ex_13
ex_14[4] = 6 #Here I have replaced the 4th index value with 6 & also applicable for ex_13
print("this is the output of ex_13 --> "+str(ex_13))
print("this is the output of ex_14 --> "+str(ex_14))

print("----------------------------------------------------------")

major_cities4 = ("Tokyo", "London", "New York", "Shanghai", "Sydney")
print(major_cities4[::-1])





