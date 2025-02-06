'''
    Problem 3
    Write a Python program that takes a positive integer as input and prints the sum of its digits.
    Ex:
    Input: 123
    Output: The sum of digits is 6 (1 + 2 + 3).
'''

import math


num = int(input("Enter a positive integer: "))
sum = 0

while num > 0:
    sum = sum + num % 10
    num = math.floor( num / 10)

print(f"The sum of digits is {sum}")