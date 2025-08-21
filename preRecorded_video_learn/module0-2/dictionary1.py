a ={"name":"rahim","karim": 15, 'fahim':28 , "rogar": 32, 99:[1,2,3,4] }
# print(type(a))

# for i in a:
#     print(i)
# print("-----------------------------")
# for i in a.values():
#     print(i)


# print(a.keys(),a.values())



# for k,v in a.items():
#     print(f"key name: {k}, value: {v}")

a = [1,2,3,4]
b = ['Mango', 'Banana', 'Orange', 'Apple' ]


# print(zip(a,b))
# print(list(zip(a,b)))
# print(dict(zip(a,b)))

# c = zip(a,b)
# print(c)
# print(list(c))
# print(dict(zip(a,b)))


c = dict(zip(a,b))
print(c[1])

print('======================')
d = dict(zip(b,a))
print(d['Apple'])

