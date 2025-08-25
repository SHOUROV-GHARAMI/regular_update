# array_list = []
# array_size = int(input("Enter array size: "))
# for i in range(array_size):
#     value = int(input("Enter an integer: "))
#     array_list.append(value)
# print(array_list)
array_list = [5,4,3,2,1]
def sort_array_list(array_list):
    for i in range(len(array_list)-1, 0 , -1):
        for j in range(i):
            if array_list[j] > array_list[j+1]:
                temp = array_list[j]
                array_list[j] = array_list[j+1]
                array_list[j+1] = temp

sort_array_list(array_list)
print(array_list)