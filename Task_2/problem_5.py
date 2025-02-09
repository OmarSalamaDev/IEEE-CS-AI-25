'''
    Create a program that reads a text file,
    counts the occurrences of each word, and prints the results.
'''


file = open("simple_text.txt", "r")
text = file.read()
file.close()

words = text.split()

wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

print(wordCount)