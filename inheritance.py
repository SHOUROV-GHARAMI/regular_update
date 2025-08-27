#nheritance allows us to define a class that inherits all the methods and properties from another class.
'''
Here's a breakdown of the distinction:
Function: A function is a block of (reusable) code that performs a (specific task). It can be defined independently and called directly by its name. Functions can take arguments and return values.
--------------------------------------------------------------
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Alice"))                     # Calling a standalone function
-------------------------------------------------------------
Method: A method is a function that is defined within a class and is called on an instance (object) of that class. Methods typically operate on the (data) (attributes) of the object they belong to and define the behaviors of that object. They implicitly receive the instance itself as their first argument, conventionally named self.
----------------------------------------------------------------
    class Dog:
        def __init__(self, name):
            self.name = name

        def speak(self):                     # This is a method
            return f"{self.name}               says Woof!"

    my_dog = Dog("Buddy")
    print(my_dog.speak())                     # Calling a method on an object
---------------------------------------------------------------
In essence, the key difference lies in their association: functions are standalone, while methods are bound to objects and classes, allowing them to interact with the object's state.
'''
class Phone:                                      #Parent class, Super class, Base class         
    def call(self):
        print("You can print")
    def message(self):
        print("You can message")

class Samsung(Phone):                            #Child class, sub class, Derived class
    ##call, message came from class Phone via (Phone) we inherited all the methods and properties from another class Phone
    # def call(self):
    #     print("You can message")
    # def message(self):
    #     print("You can message")
    def photo(self):
        print("You can take photo")

# p = Phone()
# p.call()
# p.message()

s = Samsung()
s.call()
s.message()
s.photo()

print(issubclass(Samsung,Phone)) #to chack class Phone's sub class Samsung ?