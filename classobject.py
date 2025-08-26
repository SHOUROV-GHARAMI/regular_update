# class Student:
#     roll = ""
#     gpa = ""
#     studentclass = "" 
# rahim = Student()
# karim = Student()

# # -------------------print(isinstance(rahim,Student)) # to find is rahim object is in Student class
# #-------------------- print(isinstance(karim,Student)) # # to find is karim object is in Student class
# rahim.roll = 101
# rahim.gpa = 3.78
# rahim.studentclass = 10
# print(f"Rahim Roll = {rahim.roll} ,GPA  = {rahim.gpa}, Class = {rahim.studentclass}")


# karim.roll = 102
# karim.gpa = 3.50
# karim.studentclass = 11
# print(f"Karim Roll = {karim.roll} , GPA = {karim.gpa}, Class = {karim.studentclass}  ")

# ----------------------------------------------------------------------------------------------------------------------------------------------
#class, object, function

# class Student:
#     name = ""
#     roll = ""
#     gpa = ""
    
#     def set_value(self,name,roll,gpa):         #here self,name,roll,gpa is an arguments
#         self.name = name
#         self.roll = roll
#         self.gpa = gpa

#     def display(self):                    #here self is an argument 
#         print(f"Name = {self.name}, Roll = {self.roll} , GPA = {self.gpa}")

# student1 = Student()
# student1.set_value("Rahim", 101, 3.78)
# # student1.name = "Rahim"
# # student1.roll = 101
# # student1.gpa = 3.78
# student1.display()

# student2 = Student()
# student2.set_value("Karim", 102, 3.78)
# # student2.name = "Karim"
# # student2.roll = 101
# # student2.gpa = 3.78
# student2.display()


# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
#class, object, function practice

# class Student:
#     roll = ""
#     gpa = ""
#     def set_value(self,roll,gpa):
#         self.roll = roll
#         self.gpa = gpa

#     def display(self):
#         print(f"Roll= {self.roll}, GPA= {self.gpa}")

# rahim = Student()
# rahim.set_value(101,3.76)
# rahim.display()

# karim = Student()
# karim.set_value(102, 3.66)
# karim.display()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#contructor is a special type of method(function) where we don't have to call extra to set values

# class Student:
#     roll = ""
#     gpa = ""

#     def __init__(self,roll,gpa):                 #here __init__ is a constructor for value initialization of rahim and karim student
#         self.roll = roll
#         self.gpa = gpa

#     def display(self):
#         print(f"roll = {self.roll}, gpa = {self.gpa}")

# rahim = Student(101, 3.76)
# rahim.display()

# karim = Student(102, 3.54)
# karim.display()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#practice

class Triangle:
    # base = "" / not need here 
    # hight = "" / not need here 

    def __init__(self,base,hight):
        self.base = base
        self.hight = hight

    def calculate_area(self):
        area = 0.5 * self.base *self.hight
        print(f"Area = {area}")

t1 = Triangle(10,20)
t1.calculate_area()

t2 = Triangle(20,30)
t2.calculate_area()