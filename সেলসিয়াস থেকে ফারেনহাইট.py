'''

Celsius to Fahrenheit

Problem Statement
Write a program to convert temperature from Celsius to Fahrenheit.

Input
The input consists of a float number.

Output
Output will be the Fahrenheit value.

Constraints
The program should print the number with exactly two decimal points.
Example:
Enter the temperature in Celsius

Input:
32
Output:
The temperature in Fahrenheit is: 89.60

সেলসিয়াস থেকে ফারেনহাইট

সমস্যার বিবরণ
এমন একটি প্রোগ্রাম লিখ যেখানে সেলসিয়াসকে ফারেনহাইট স্কেলে রূপান্তরিত করা হবে।

ইনপুট
ইনপুট হবে দুইটি ফ্লোট সংখ্যা।

আউটপুট
আউটপুট হবে ফারেনহাইট।

সীমাবদ্ধতা
প্রোগ্রামটি সবসময় শুধুমাত্র দশমিকের পর দুই ঘর পর্যন্ত প্রিন্ট করবে।
উদাহরণ:
Enter the temperature in Celsius

ইনপুট:
32
আউটপুট:
The temperature in Fahrenheit is: 89.60
'''

# -*- coding: utf-8 -*-
# Write Python code from here


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input())
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
