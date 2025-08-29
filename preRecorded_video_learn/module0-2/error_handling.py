# Errors vs Exceptions
'''
# compile Time --> error
# error occor's in 
--> syntax, indentation, clone, space etc.

#  Run Time --> Exception
# Exception error occur's when
When i have 10 item list , but i want 15'th item .
when we run that code it occur a error while running the program.
indexing error , value error, zero division error
'''


# Exception error -->
# try: # je code e exception thakte pare
#     with open('rahim.txt', 'r') as f:
#         print(f.read())  # FileNotFoundError: [Errno 2] No such file or directory: 'rahim.txt'

# except FileNotFoundError: # here we put error massage
#     print("file not found")


# try: # je code e exception thakte pare
#     print(10/0)
# except ZeroDivisionError: # here we put error massage
#     print("Erro: Division by Zero is not possible")
# here if code find it's first error it will not run other error 

# try: # je code e exception thakte pare
#     print(int("abc"))
# except ValueError: # here we put error massage
#     print("Invalid value")


# try: # je code e exception thakte pare
#     a = [1,2,3,4,5]
#     print(a[100])
# except IndexError: # here we put error massage
#     print("Invalid Index")


# try: # je code e exception thakte pare
#     a = 123 #abc
# except Exception as e: # here we put error massage
#     print("Some error occurred!!", e)
# else:
#     print("code executed successfuly")
# finally:
#     print("it will print")



# class InvalidFileTypeError(Exception):
#     pass
# filename = input("Enter file name: ")
# try:
#     if not filename.endswith(".csv"):
#         raise InvalidFileTypeError("Only .csv files are allowed!")

#     with open(filename, "r") as f:
#         print("Reading file successfully...")

# except InvalidFileTypeError as e:
#     print("Custom Error:", e)

# except FileNotFoundError:
#     print("Error: File not found.")


#manual error triger

# check_file('data.csv')
# # check_file('data.txt')

# def check_file(filename):
#     if not filename.endswith(".txt"):
#         raise ValueError("Only .txt files are allowed")
#     print('Valid file')

# custom error handling
# def check_file(filename):
#     if not filename.endswith('.text'):
#         raise ValueError("Only .txt files are allowed")
# print("valid file")
# try:
#     check_file('data.csv')
# except Exception as error:
#     print(error)