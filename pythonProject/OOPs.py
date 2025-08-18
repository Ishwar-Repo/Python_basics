# OOPs,=Object Oriented Programming, Thera are 4 Pillars of OOPs concepts
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance and
# 4. Polymorphism.


# Classes and Objects :-
# Now before we get started with learning what are classes and objects, let's first understand the need to go for classes and objects.
# Classes - classes are a logical collection of attributes and methods and objects are instances of class.
# OR- A class is a blueprint while an object is an execution of that blueprint


# check if an employee has achieved his weekly target or not.
class Employee:
    name="Ben"
    designation="Sales Executive"
    salesMadeThisWeek=4
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek>=5:
            print("Target has been achieved")
        else:
            print("Target has not been achieved")

employee1=Employee()
employee2=Employee()
print(employee1.name)
print(employee2.name)
employee1.hasAchievedTarget()

# Everything in Python is an object.
# So what do I mean to say by that ? Let's say you have a List called numbers with the numbers as 1, 2 and 3 as a part of your list.
# Now we have a function in Python called type(), which checks the data type of variable. Now if you check the type of numbers you will see
# that it belongs to class list. Now list is a class that comes with Python. And what you have done now is to create an object for that list.
# So numbers is an object of your class list. So that's the reason when you perform operations on lists  such as numbers.append(), there
# is an append method as a part of your class list which performs this operation. So when I say numbers.append(4), what happens
# internally is the append method of your list class is being invoked, and it updates your list as 1,2,3 and 4.