'''
    Problem 8
    Write a Python program that checks if a given word is a palindrome.
    A palindrome is a word that reads the same backward as forward.
    Input: "level"
    Output: "The word 'level' is a palindrome."

    Input: "python"
    Output: "The word 'python' is not a palindrome."
'''

word = input("Enter a word: ")
word = word.lower()

if(word == word[::-1]):
    print(f"The word '{word}' is a palindrome.")
else:
    print(f"The word '{word}' is not a palindrome.")