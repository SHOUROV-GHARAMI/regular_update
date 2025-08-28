# def my_function(f_name, l_name, age):
#     print(f"My name is {f_name} {l_name}. My age {age}.")

# my_function(age = 25,l_name = "khan",f_name = "Rahim")


#Arbitary Number of key word aggumants
def my_func(**kwargs):
    # print(kwargs)
    print(f"My name is {kwargs['f_name']} {kwargs['l_name']} . I am {kwargs['age']} years old. I got {kwargs['marks']} in programing. I live in {kwargs['address']}.")

my_func(age = 25 , l_name = "khan", f_name = "Rahim",  marks = 95, address = "Dhaka")