#Program that Replace Vowels with Asterisks and Print the Result
'''
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for character in sentence:
    if character in vowels:
        sentence = sentence.replace(character, "*")
print(sentence)
'''
#write a program that prients the numbers from 1 to 10 using a for loop.
'''
for i in range (1, 11):
    print(i)
'''
#Write a program that asks the user to enter a number, and then prints the number table for that number up to 10.
'''
num = int(input("Enter a number: "))
for number in range(1, 11):
    print(f"{num} X {number} = {num * number}")
'''
