# Python Program that Removes All Vowels From a Given String and returns a new string with all of the vowels removed.

string = str(input("Enter a string: "))
vowels = "aeiouAEIOU"
count = 0
result = ""
for character in string:
    if character not in vowels:
        result += character
print(result)