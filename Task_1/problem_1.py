'''
    > Problem 1
    Write a program that takes numbers as input from the user,
    terminates when the user enters -1, and prints the sum of all the entered numbers.
    Ex:
    Input: 4 8 15 16 23 42 -1
    Output: Sum: 108
'''

sum = 0 
print("Enter positve integers or -1 to stop")
userInput = int(input("> "))

while userInput != -1:
    sum = sum + userInput
    userInput = int(input("> "))

print(f"Sum is: {sum}")
