# {}
# key value pair
# indexing er shujog nai
# key gula obossoi immutable

a = {'rahim':12, 'karim': 15,'fahim':78, 1:[2,3,4,5,2], 2:{2,4,5,6,7}}

print(a)
print(type(a))
for i in a:
    print(i)
print('-------------------------------')
for i in a.values():
    print(i)
print('-------------------------------')
print(a.keys(), a.values())
print('-------------------------------')
for k,v in a.items():
    print(f"Key Name : {k}, Values = {v}")
print('-------------------------------')

a = [1,2,3,4]
b = ["Mango","Banana","Apple","Orange"]

c = dict(zip(a,b))
e = dict(zip(b,a))
print(dict(zip(a,b)))

print(c)
print(e)

print(c[1])