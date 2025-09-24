#Write a program to count the number of vowels in a string. | For Loop

string = str(input("Enter a string: "))
vowels = "aeiouAEIOU"
count = 0
for character in string: #for loop for each character
    if character in vowels: 
        count += 1
print(f"The number of vowels in the string is {count}.")






















'''
for character in 'abcdefg':
    print(character)
numbers = [1,2,3,4,5,6,7]
for number in numbers:
    print(number)
'''
