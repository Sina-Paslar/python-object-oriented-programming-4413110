# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.commen = "Class A"


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.commen = "Class B"


class C(B, A):
    def __init__(self):
        super().__init__()

    def showProps(self):
        print(self.prop1)
        print(self.prop2)
        print(self.commen)


print(C.__mro__)
c = C()
c.showProps()
