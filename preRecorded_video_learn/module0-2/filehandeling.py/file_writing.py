# with open("name1.txt", 'w') as file: # 'w' write/overwrite
#     file.write("Hello world.\n") 
#     file.write("I am writing in a file.\n") 

# with open('name1.txt', 'a') as f: # 'a' append 
#     f.write("Hi, Hello world.\n") 
#     f.write("World of programming.\n") 
#     f.write("Happy world.\n") 

# lines = ['Web Developer \n', "Software Quality tester \n"]
# with open('name1.txt', 'a') as f:  string array append
#     f.writelines(lines)

#if file exist or not
# import os 
# if os.path.exists('name1.txt'):
#     print("file exist")
# else:
#     print('file not found')

# import os 
# if os.path.exists('file.txt'):
#     print("file exist")
# else:
#     print("file not found")



# import pathlib
# file_path = pathlib.Path("name.txt")
# if file_path.exists():
#     print("file exist")
# else:
#     print("file not found")
'''
import os
import pathlib

file_path = pathlib.Path('name.txt')
if file_path.exists():
    print("file exists")
print(os.path.abspath('name.txt')) # file path
print(os.path.getsize('name.txt'))  #file size bytes
'''
# with open('name.txt', 'r') as f:
#     print(f.read(13))       # read 13 character form file
#     print(f.tell())         # tell where is coursor place