'''
# The word Polymorphism means "many forms".
# In Python OOP, polymorphism allows one function, method, or operator to behave differently depending on the object or data type it is working with.

👉 Simply: The same interface can be used for different types of objects.
Why do we need Polymorphism?
# Ensures consistent interfaces across different classes.
# Allows objects to respond differently to the same method call.
# Promotes loose coupling by relying on shared behavior, not specific types.
# Enables writing flexible, reusable code that works across types.
# Simplifies testing and future extension of code.
'''
# print(len("Shourov Gharami"))
# print(len([1,23,4,5,6,67,88,899]))

# def add(x, y, z = 0):
#     return x + y + z
# print(add(10,20))
# print(add(2,3,4))

#1. Compile-time Polymorphism (a.k.a. Method Overloading 🚫 not natively supported in Python)

# class Math:
#     def add(self, a, b = 0, c = 0):
#         return a + b + c
# m = Math()

# print(m.add(5, 10))
# print(m.add(5, 10, 20))

#2. Run-time Polymorphism (Method Overriding ✅ supported in Python)
'''
# When a child class provides its own implementation of a method that is already defined in the parent class.
# Achieved through inheritance.
'''
# class Animal:
#     def sound(self):
#         return "Some generic sound"
# class Dog:
#     def sound(self):
#         return "Bark"
# class Cat:
#     def sound(self):
#         return "Meow"
# animals = [Dog(), Cat(), Animal()]
# for a in animals:
#     print(a.sound())

# 3. Polymorphism with Functions/Operators
'''
# Python operators and functions can behave differently based on data type.
'''
# print(10 + 5)
# print("Hello" + "World")

# print(len("Python"))
# print(len([1,2,3,4,5,6,7,8,9]))
'''
🔹 When Do We Use Polymorphism?
We use polymorphism when:
# We want to write flexible and reusable code that works with different types of objects.
# When designing frameworks, libraries, or APIs where exact implementation is left to the user.
# To implement dynamic behavior depending on object type.

🔹 Functionality / Benefits
✅ Increases code reusability.
✅ Reduces code duplication.
✅ Makes code extensible (easy to add new classes without changing existing logic).
✅ Makes programs more intuitive and closer to real-world modeling.
'''

#paymentSystem

# class Payment:
#     def pay(self, amount):
#         pass

# class CreditCard(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card.")

# class PayPal(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using PayPal.")

# payments = [CreditCard(), PayPal()]
# for p in payments:
#     p.pay (100)