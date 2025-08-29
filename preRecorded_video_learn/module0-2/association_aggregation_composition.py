#Association relationship : uses-a relationship between two classes.-- 
# Aggregation is a special type of Association, where one class contains a reference to another class, but both can still exist independently.
#One class uses another, but ther are independent entities 
#There's no strong ownership - they just collaborate- The container object doesn’t own the contained object.


#👉 Here, Driver uses Car, but neither owns the other. If Driver is deleted, the Car still exists.
class Driver:
    def __init__(self,name):
        self.name = name
    def drive(self, car):
        print(f'{self.name} is driving {car.brand}')
class Car:
    def  __init__(self, brand):
        self.brand = brand
car = Car('Toyota')
driver = Driver('John')
driver.drive(car)


#👉 Department has employees, but employees can exist without the department.
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = [] # aggregation
    
    def add_employee(self, employee):
        self.employees.append(employee)
class Employee:
    def __init__(self, name):
        self.name = name
e1 = Employee("Alice")
e2 = Employee("Bob")
dept = Department("IT")
dept.add_employee(e1)
dept.add_employee(e2)
print([emp.name for emp in dept.employees]) #['Alice', 'Bob']

#student, Laptop

# class Laptop:
#     def __init__(self, brand):
#         self.brand = brand

# class Student:
#     def __init__(self, name, laptop_obj):
#         self.name = name
#         self.laptop_variable = laptop_obj

#     def show_laptop_info(self):
#         print(f'{self.name} has a laptop named {self.laptop_variable.brand}') 
#         #here assined laptop brand via (self.laptop_variable.brand)

# laptop1 = Laptop("Asus")
# student = Student("Rahim",laptop1) # here we assined laptop1 into Student class

# student.show_laptop_info()


#Aggregation : has a relationship
#A university has departments

# class Department:
#     def __init__(self, name):
#         self.name = name 