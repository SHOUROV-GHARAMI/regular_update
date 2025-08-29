'''
🔎 What is Scope Resolution in Python?
# Scope → defines where a variable (or name) is accessible.
# Scope resolution → the process Python uses to figure out which variable a name refers to when it is used.
# Python follows the LEGB Rule (Local → Enclosed → Global → Built-in) to resolve variable names.
'''
# Local (L)
# Names inside the current function.

# def func():
#     x = 10   # local
#     print(x) # resolves to local


# Enclosed (E)
# Names in outer functions (when functions are nested).

# def outer():
#     x = 20   # enclosed variable
#     def inner():
#         print(x)  # finds in enclosing scope
#     inner()
# outer()


# Global (G)
# Names defined at the top-level of the script/module.

# x = 30   # global variable
# def func():
#     print(x)  # resolves to global variable
# func()


# Built-in (B)
# Python’s built-in names (like len, sum, print).

# print(len("hello"))  # resolves to built-in len


# x = 10              #Global variable
# def func():
#     x = 19             #local variable
#     y = 20             #local variable
#     print("x",x)
#     print('y',y)

# func()
# print(x)



# n = "global"        #global variable
# def outer():
#     n = "enclosing"     #Enclosing variable
#     def inner():
#         global n  #here it change global variable n = "global" to n = "local"
#         nonlocal n  #here it change Enclosing variable n = "enclosing" to n = "local"
#         n = "local"   #local variable
#         print(n)
#     inner()
#     print(n)
# outer()
# print(n)


#global  --> change global variable  , not enclosing
# nonlocal --> change enclosing variable, not global


