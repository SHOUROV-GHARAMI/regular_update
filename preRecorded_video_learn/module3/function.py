# hello = print("hello")
# print("hello"*2)
# user_name = input("Enter your name: ")
# # built in function -- print(),input(),sum(),math() etc
# # unbuilt in functon -- customize functon



# maximum = max([0,1,2,3,4,5,6,7,8,9])
# print(f"Here max value is: {maximum} and after multiply by 3 the result will be: {maximum * 3}")

# minimum = min([0,1,2,3,4,5,6,7,8,9])
# print(f"Here minimum value is : {minimum} and after multiply by 3 the result will be: {minimum * 3}")

# name = str(input("Type your name: "))
# def custom_function(name):
#     print(f"Hello Mr. {name} \n What you do ? ")
# custom_function(name)



def custom_function(name = str(input("Type your name: "))):
    print(f"Hello Mr. {name} \n What you do ? ")
custom_function()