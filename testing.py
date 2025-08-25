# #TEST ON THE GO
# a = 20.67
# b = int(a)
# print(b)
# print(type(b))
# print(a)
# print(type(a))
# --------------------------------------------------------------
# str
# int
# bool
# None
# float
# ----------------------------------------------------------------------
# x = " kanfkdsf saghg jdgshg  fdfh hhs "
# print(len(x))


# ---------------------------------------------------
# password = str(input("enter password: "))
# if len(password) < 8:
#     print("password is too short")
# elif len(password) > 15:
#     print("Password is too big")
# else:
#     print("password is ok now")

# x = " My name is shuvo,\n I am an software engineer,\n I am from dhaka bangladesh"
# print(x)

# x =  " My name is shuvo, I am an software engineer, I am from dhaka bangladesh"
# print(x)
# print(" My name is shuvo,\t I am an software engineer, I am from dhaka bangladesh")
# print(" My name is shuvo,\b I am an software engineer, I am from dhaka bangladesh")

# print(" My name is shuvo,\f I am an software engineer, I am from dhaka bangladesh")

# print("This is the first page.\fThis is the second page.")

# print("Another way to use form feed:\x0c")

# -------------------------------------------
# x = []
# for i in range(1000):
#     i+=1
#     x.append(i)
# print(x)


# x = 'The Teacher said," today\'s exam is postponed "'
# print(x)

#\r: Represents a carriage return, moving the cursor to the beginning of the current line.


# x = 'The Teacher said," today\rs exam is postponed"'
# print(x)

# x = 'the Teacher said," today\'s exam is postponed"'
# x = x.capitalize()
# y = x.upper()
# z =x.lower()
# print(x,"\n")
# print(y,"\n")
# print(z)

# import math
# math.

# import math
# print(math.cos(100))


# a = 5
# b = 10
# a,b = b,a
# print(f"after swaping a = {a} and b = {b}")

# x = 31
# if x%2 == 0:
#     print(x)

# x = "Shourov Gharami"
# print(x[1:-2])


# count = 0
# while count <= 10:
#     value = count
#     print(count)
#     count = count + 1
# print(value)


# a = 1
# while  a <= 10:
#     print("A is ", a)
#     a = a + 1
# print("Done printing finally, Free!!")

# example of list
# a = [1,2,3,4,5] #here a is list and here multiple value is assingned in list 
# print(type(a))

# a = 10
# a = 20
# #here value of a = 10 is replaced with a = 20 

# fruits = ["apple", "banana", "apple"]
# items = [True, 5.2,"Yo"]
# print(fruits[0])
# fruits[0] = "cherry" #here in fruits list we mutade apple into cherry .
# print(fruits)

# example of typle

# fruits = ("Apple", "Banana", "Orange")
# fruits[0] = "cherry" #here we can't change value in typle or perform mutation
# print(fruits)


#list slicing

# list1 = ["Apple", "Banana", "Cherry", "Orange", "Mango"]
# print(list1[0:2])
# print(list1[2:])
# print(list1[:-1])
# print(list1[-3:-1])
# print(list1[0:5:2]) #list[start : stop : step] // using list slicing create a new list

# Values = [10, 20, 30, 40, 50, 60, 70]
# print(Values[0:5:2]) #list[start : stop : step]


# list1 = ["Apple", "Banana", "Cherry", "Orange", "Mango"]
# print(list1[0:len(list1):2])



#Operators on List and and Tuple in python 

# list1 = ["apple", "banana", "cherry", "mango"]
# list2 = [20,30,40,50, {(30 + 40)}]
# addition = list1 + list2
# print(addition)

#list compare
# a = [5,6,7,8,9,23,776]
# b = [343,6467,888,99,0,53]
# if a > b:
#     print("a is grater then b")
# else:
#     print("b is grater then a")


# typle compare
# a = (5,6,7,8,9,23,776)
# b = (343,6467,888,99,0,53)
# if a > b:
#     print("a is grater then b")
# else:
#     print("b is grater then a")

# list methods 
# a = [1,2,3,4,5,6,7]
# a.append(20)
# print(a)

# b = ["a", "b", "c","d","e"] 
# a.extend(b)
# print(a)

# a.insert(1, "z") #here 1 is index of list a // and here z is the value
# print(a)

#a.reverse()  // #his method modifies the original list in-place. It does not create a new list; instead, it reorders the elements within the existing list.
# print(a) 

# fruits = [
#     ["apple", "Banana"], 
#     ["Cherry","Mango"]
#     ]
# print(fruits[2][2][0]) #//IndexError: list index out of range // here 2 is out of range


# fruits = [
#     ["apple", "Banana"], 
#     ["Cherry","Mango"]
#     ]
# print(fruits[1][1][0]) #//here [1] is the second item of fruits list,here [1] is the second item's second list of fruits list ,here [0] is the second item's second list of index 0 value  of fruits list

# fruits = [["apple", "Banana"], {"Cherry","Mango"}]
# print(list(fruits[1])[0]) 

# set is unordered , unchangeable,unindexed, unique, and partially unchangeable 
#we can do in using set union, intersection, difference
# fruits_set = {"apple", "banana", "cherry", "mango"}
# print(fruits_set[0]) #//TypeError: 'set' object is not subscriptable

# my_set = [3, 1, 4, 1, 5, 9, 2, 6]
# print(sorted(my_set))

# my_set = {3, 1, 4, 1, 5, 9, 2, 6}
# sorted_list = sorted(my_set) #here new variable is assinged to perform sorting
# print(sorted_list)


# set1 = {1,2,3,4,5,6,7,8,9,"apple", "banana", "cherry", "mango"}
# set2 = {2,3,6,7,8,90,3,1,5, "A", "B", "C"}

# print(set1|set2) # union set
# print(set1.union(set2))# union set

# print(set1 & set2) #intersection
# print(set1.intersection(set2)) #intersection

# print(set1-set2) #difference 
# print(set1.difference(set2)) #difference 



# Dictionary = it a collection of two items in packed .// it's simply key-value mapping
# student = {
#     "name": "Arif",
#     "class": 10,
#     "subject": "Bangla",
#     "mark": 87,
#     "is_valid": True
# }
# # print(student)
# # print(student["name"])
# # print(student["class"])
# # print(student["subject"])
# # print(student["mark"])
# # print(student["is_valid"])


# # dict_items = student.items()

# print(student.keys())
# print(student.values())

# fruits = ["apple", "Banana", "Cherry","Mango"]
# for items in fruits:
#     print(items)

# number_list = [1,2,3,4,5,6,7,8,9,11,"Hello"]
# for item in number_list:
#     print(item)
    

# n = int(input("Enter size of array: "))
# array = []
# item = 0
# while item < n:
#     element = int(input("Enter element: "))
#     array.append(element)
#     item = item + 1
# print(array)

# n = int(input("Enter size of array: "))
# array = []
# item = 0
# while item < n:
#     element = int(input("Enter element: "))
#     array.append(element)
#     item = item + 1
# print(array)


# n = int(input("Enter array size: "))
# array = []
# for item in input("Enter array element: ").split():
#     array.append(int(item))
# print("Array", array)

#simple array input 

# array = []
# for item in input("enter element: ").split():
#     array.append(int(item))
# print("array",array)

# array = []
# print("Enter number (type 'stop' to finish): ")
# while True:
#     value = input()
#     if value == "stop":
#         break
#     array.append(int(value))
# print("array", array)


# array = []
# print("Enter number (type stop to finish):")
# while True:
#     value = input()
#     if value == "stop":
#         break
#     array.append(int(value))
# print("array", array)

