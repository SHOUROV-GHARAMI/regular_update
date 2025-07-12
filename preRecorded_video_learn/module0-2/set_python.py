
# a = [1,2,2,3,3,4,5,6,7,8]
# s = set(a)
# # s[0] = 100 # set' object does not support item assignment
# # print(s[0])# 'set' object is not subscriptable
# print(s)

# Union, Intersection
a = {1,2,3,4}
b = {3,4,5,6}
d = a.union(b)
c = a.intersection(b)
print(c)
print(d)