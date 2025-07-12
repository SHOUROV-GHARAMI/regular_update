a = [1,2,3,4,5,6,7,8,9,45,"a",68,13,686,]
for i in a:
    if type(i) == str:
        break # here we are breaking the loop when our desire type found
    else:
        print(i)
print("------------------")
for i in a:
    if type(i) == str:
        continue #here we are ignoring str value in it.
    else:
        print(i)