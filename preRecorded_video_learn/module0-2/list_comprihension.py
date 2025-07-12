##normal way
# a = [1,2,3,4,5,6,7,8,9]
# result = []
# for i in a:
#     if i % 2 == 0:
#         result.append(i)
# print(result)

###########################################
# a = [12,43,54,66,33,663,588,655,556,778,99]
# result2 = []
# for i in a:
#     if i % 2 == 0:
#         result2.append(i)
# print(result2)
################################################
b = [1,2,3,4,5,6,7,8,9]
b_new = []
for i in b:
    if i % 2 == 0:
        b_new.append(i**2)
    else:
        b_new.append(i)
print(b_new)
#######################################
##list comprehension 
# new_result = [i for i in a if i % 2 == 0]
# print(new_result)

###########################################
# a = [12,43,54,66,33,663,588,655,556,778,99]
# new_result2 = [i for i in a if i % 2 == 0]
# print(new_result2)

############################################
# b = [1,2,3,4,5,6,7,8,9]
# b_new = [i**2 if i % 2 == 0 else i for i in b ]
# print(b_new)