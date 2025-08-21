def my_function(f_name, l_name, age, birth_year):
    print(f"My name is {f_name} {l_name}. My age is {age} years. My birth year is {birth_year}.")
# my_function("Tipu","Khan",32, 2000)
# user_info= my_function("Tipu","Khan",32, 2000)
# user_info= my_function("Khan","Tipu", 2000, 32) #undefine
user_info = my_function(l_name ="Khan",f_name ="Tipu",birth_year =2000, age =32) #define parameter 
print(user_info)