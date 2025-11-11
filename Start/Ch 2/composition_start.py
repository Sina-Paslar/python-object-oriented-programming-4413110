# Python Object Oriented Programming by Joe Marini course example
# Using composition to build complex objects


class Book:
    def __init__(self, title, price, author = None):
        self.title = title
        self.price = price

        self.author = author

        self.chapters = []

    def addchapter(self, chapter):
        self.chapters.append(chapter)

    def getBookPageCount(self):
        result = 0
        for page in self.chapters:
            result += page.pageCount
        return result

class Author():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    
    def toString(self):
        string = f"{self.firstName} {self.lastName}"
        return string

class Chapter():
    def __init__(self, name, pageCount):
        self.name = name
        self.pageCount = pageCount
        
authorForb1 = Author("Leo", "Tolstoy")
b1 = Book("War and Peace", 39.0, authorForb1)


b1.addchapter(Chapter("Chapter 1", 125))
b1.addchapter(Chapter("Chapter 2", 97))
b1.addchapter(Chapter("Chapter 3", 143))

print(b1.title)
print(b1.getBookPageCount())

# for auth in b1.author:
#     print(auth.firstName)
#     print(auth.lastName)
# print(b1.author)
