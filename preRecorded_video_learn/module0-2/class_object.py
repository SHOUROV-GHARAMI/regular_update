class Employee:
    company_name = "Ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary #by convention,(_vaiable) emon hole it's private dora hoy , but logically it's not private for private we have to use (setter and getter), here _salary is private 

    def get_salary(self, password):
        if password == "admin":              # password = admin  
            print(self._salary)
        else:
            print("Invalid Access!!")

    def set_salary(self, password, salary):
        if password == "admin":                 # password = admin  
            self._salary = salary
            print(f"New Salary: {self._salary}")
        else:
            print("Invalid Access!!")

obj1 = Employee("Rahim", 30000)
obj2 = Employee("Karim", 50000)

obj1.get_salary("admin")
obj1.set_salary("admin",70000)

obj1._salary= 2   # whithout password one can easyly update / assess the value
print(obj1._salary)
print(f"Rahim's Salary: {obj1._salary}")

obj1.get_salary("admin")
