class Employee:
    company_name = "ostad Company"
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):  #AttributeError: property '_salary' of 'Employee' object will became read only, for thie we can not update _salary value.
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


obj1 = Employee("Rahim", 40000)
# print(obj1.get_salary)
print(obj1.salary)



# print(obj1._salary)  #AttributeError: property '_salary' of 'Employee' object has no setter