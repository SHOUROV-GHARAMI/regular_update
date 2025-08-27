'''
the are three types of inheritance
1. Hierarchical inheritance
2. Multi-level inheritance
3. Multiple inheritance
'''
'''
Hierarchical inheritance example
Shape class--Triangle
Shape class--Rectangle
'''
# class Shape:
#     def __init__(self,dim1,dim2):
#         self.dim1 = dim1
#         self.dim2 = dim2
#     def area(self):
#         print("Hello area")


# class Triangle(Shape):
#     def area(self):
#         area = .5 * self.dim1 * self.dim2
#         print(f"Area of Triangle: {area}")

# class Rectangle(Shape):
#     def area(self):
#         area = self.dim1 *self.dim2
#         print(f"Area of Rectangle: {area}")

# t1 = Triangle(20,30)
# t1.area()

# r1 = Rectangle(20,30)
# r1.area()
'''
Multilevel inheritance example
A class--B class--c class
'''
# class A:
#     def display1(self):
#         print("I am inside A class")

# class B(A):
#     #display1() 
#     def display2(self):
#         print("I am inside B class")

# class C(B):
#     #display2()
#     def display3(self):
#         super().display1()
#         super().display2()
#         print("I am inside C class")

# object1 = C()
# # object1.display1()
# # object1.display2()
# object1.display3()
'''
Multiple inheritance example
A class -- B class and C class -- D class
'''
class A:
    # def display1(self):
    def display(self):
        print("I am inside A class")

class B: 
    # def display2(self):
    def display(self):
        print("I am inside B class")

class C(A,B):
    pass
    # def display3(self):
    #     # super().display1()
    #     # super().display2()
    #     # print("I am inside C class")

object1 = C()
# object1.display3()
object1.display()

