# file = open('name.txt', 'r') # file open( name of the file, what to do after opening the file)
# content = file.read() # file read kore variable(content) a rakhlam
# print(content)

# file = open('wikitext.txt', 'r')
# data = file.read()
# print(data)
# file.close()

# with open('name.txt', 'r') as file:
#     contant = file.read()
#     print(contant)


with open('wikitext.txt', 'r') as file:
    content = file.read()
    print(content)