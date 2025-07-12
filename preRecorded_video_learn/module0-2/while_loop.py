# a = [1,2,3,4,5,6,7,8,9]
# result = 0

# i = 0
# n = len(a)
# while i<n:
#     result = result + a[i]
#     i+=1 #i=i+1

# print(a)


##############################################
a = [1,5,-45,69,9,-72,45]
i = 0
result = []
while i<len(a):
    if a[i] < 0:
        a[i] = 0
    i+=1
print(a)
