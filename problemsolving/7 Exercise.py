#Write a Program that Checks If a Word Entered by the User is a Palindrome.
'''
word = str(input("Enter a word: "))
reversed_word = ""
for character in word:
    reversed_word = character + reversed_word
if word == reversed_word:
    print("The word is a palindrome.")
else:
    print("the word is not a palindrome.")
'''