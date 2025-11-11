# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    _bookList = None

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES
    # TODO: create a static method
    def getBookList():
        if (Book._bookList == None):
            Book._bookList = []
        return Book._bookList
        
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, bookType):
        self.title = title
        if (not bookType in Book.BOOK_TYPES):
            raise ValueError
        else:
            self.bookType = bookType


# TODO: access the class attribute
print(Book.getBookTypes())

# TODO: Create some book instances
#b1 = Book("Book 1 Title", "Flase")
b2 = Book("Book 2 Title", "HARDCOVER")

# TODO: Use the static method to access a singleton object
theBookList = Book.getBookList()
theBookList.append(b2)
theBookList.append(Book("Book 3 Title", "PAPERBACK"))
for book in theBookList:
    print (f"Book title: {book.title} \nBook type: {book.bookType}")