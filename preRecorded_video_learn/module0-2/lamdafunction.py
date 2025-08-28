# def squre(x):
#     return x*x
# print(squre(5))

#variable = lamda arguments : experssion
# square = lambda x : x*x
# print(square(4))

'''
lambda function --> Unnamed
print use kora jay na
just only for returns
'''

# add = lambda a,b : a+b
# print(add(3,4))

# students = [('Rahim',60),('Karim', 59), ('Asad', 99), ('Zafor',78)]
# sorted_students = sorted(students, key = lambda x :x[1]) 
# #key = lambda x :x[1] A small anonymous function. 
# # For each tuple x, it returns the second element (x[1] → the score).
# print(sorted_students)

#map() , filter(), reduce()

#map()
# nums = [1,2,3,4,5,6,7,8,9]
# # sq_nums = list(map(want to do squre , which to apply))
# sq_nums = list(map(lambda x: x*x,nums))
# print(sq_nums)

#filter()
# nums = [1,2,3,4,5,6,7,8,9]
# even_numbers = list(filter( lambda x : x%2 == 0 , nums))
# print(even_numbers)

#reduce()
import functools

nums = [1,2,3,4,5,6,7,8,9]
sum = functools.reduce(lambda x,y : x + y, nums)
print(sum)

