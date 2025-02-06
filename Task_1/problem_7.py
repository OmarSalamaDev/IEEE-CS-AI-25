'''
    Problem 7
    Write a Python program that takes a positive integer as input and finds its prime factors.
    Input: 36
    Output: Prime Factors: 2, 3
'''

num = int(input("Enter a positive integer: "))

def isPrime(num):
    for i in range(2, num // 2 + 1, 1):
        if(num % i == 0):
            return False
    return True

for i in range(2, num // 2, 1):
    if(num % i == 0 and isPrime(i)):
        print(i, end = " ")
