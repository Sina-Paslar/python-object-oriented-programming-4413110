# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # TODO: add properties
        self.__secret = "This is secret"

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setDiscount(self, amount):
        self._discount = amount
        

# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 120)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 35.55)
b3 = Book("Basic of Economics", "Thomas Sowell", 350, 59)

# TODO: print the price of book1
print(b1.price)

# TODO: try setting the discount
print(b2.getPrice())
b2.setDiscount(0.10)
print(b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)