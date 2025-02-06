'''
    Problem 4
    Write a Python program that takes a sentence as input and prints the sentence with each word reversed.
    Ex:
    Input: "Hello World"
    Output: "olleH dlroW"
'''

sentence = input("Enter a sentence: ")
words = sentence.split()

for i in range(len(words)):
    words[i] = words[i][::-1]

print(" ".join(words))