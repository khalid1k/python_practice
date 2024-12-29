# my_list = ["khalid", "Abid", "sajjad"]
# my_list2 = [1,2,3,4,5,8,0,6,2,7,0,1]
# my_list2.sort()
# print(my_list2)

# i=0
# while i <= 2:
#     print(my_list[i])
#     i+=1

# employees = {"name": "Khalid", "Father_name": "Talib Hussain", "age": 23}
# employees["address"]= "Matta"
# for item in employees:
#     print(employees[item])

# function practice

# def table(num): 
#     for i in range(1, 11):
#         print(f"{num} X {i} = {num*i}")

# table(10)

# now write a function to display the factorial of a given number

# def factorial(num):
#     f=1
#     for i in range(1, num+1):
#         f *= i
#     return f

# result = factorial(5)
# print(f"factorial is {result}")


# exception handling in python

# try:
#     print(8+9)
# except:
#     print("you got an error")
# finally:
#     print("finally expection handling is running")

# object oriented practice

# class Student():
#     def __init__(self, name,gpa):
#         self.name = name
#         self.gpa = gpa

# st1= Student(name="khalid", gpa= 2.9)
# st2= Student(name="Abid", gpa= 3.5)
# print(f"{st1.name} and GPA is {st1.gpa}")
# print(f"{st2.name} and GPA is {st2.gpa}")

# class Agent():
#     origin = "USA"
#     def __init__(self, name, height, weight):
#         self.name= name
#         self.height= height
#         self.weight = weight

# x = Agent("khalid", 6, 72)
# print(x.weight)
# x.weight=70
# print(x.weight)
# class Circle():
#     pi=3.14
#     def __init__(self, radius):
#         self.radius= radius

#     def area(self):
#         return self.pi*self.radius*self.radius
    
# myCircle = Circle(23.5)
# print(f"my circle class radius is {myCircle.radius}")
# print(f"Area of the circle is {myCircle.area()}")


# inheritance concept

class Person():

    def __init__(self, firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
    def hello(self):
        print("hello!")

    def report(self):
        print(f"i am {self.firstName} {self.lastName}")

    
person = Person("Muhammad", "Khalid")
person.hello()
person.report()

