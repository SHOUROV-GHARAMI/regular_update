'''
An abstract method defines what must be done, but leaves how to do it to the subclasses.
Abstract Methods Use:
You use them when:
1. You have a common interface (blueprint) that all subclasses should follow
Example: Shape class → all shapes must have area() and perimeter().
2. You want to force subclasses to implement specific behavior.
3. You’re designing a framework or large system where consistency is important.
'''

from abc import ABC, abstractmethod 
#here from abc(abstract base class module) module we import "ABC"  then we implement abstractmethod  

class Shape(ABC):       
# here it's abstract base class . here ABC mean's a Helper class that provides a standard way to create an ABC using inheritance.

    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod  
# when we make a method to be abstractmethod we must use this (A decorator indicating abstract methods)
    def area(self):
        # print("Shape has no area")
        pass

class Triangle(Shape): 
# #when we inherit a abstract clss we have to have abstract method
# def area(self):
#     pass 
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Triangle",area)

class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Rectangle",area)

'''
s1 = Shape(20,30) 
s1.area() 
# when create a method to be abstractmethod we can't create it's object . here Shape(ABC) is that abstractmethod
'''

t1 = Triangle(20,30)
t1.area()

r1 = Rectangle(20,30)
r1.area()