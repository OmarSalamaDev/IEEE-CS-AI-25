'''
    Create a dictionary representing a library catalogue.
    Each book should have a title, author, and publication year.
'''

books = []
book = {}

n = int(input("Enter the number of books in the library: "))

for i in range(n):
    print(f"<book {i+1}>")
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year of publication: "))
    book["title"] = title
    book["author"] = author
    book["year"] = year
    books.append(book)

print(books)