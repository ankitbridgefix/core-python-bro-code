class Book:
    
    @classmethod
    def name(cls, last):
        cls.last = last

    @staticmethod
    def new_name():
        return 5

    @property
    def x(self):
        return self.new_name()

    def kl(self): ...
   
book = Book()
Book.name('changes')
print(book.new_name())

book_1 = Book()
book.name('small-changes')
print(book_1.new_name())
print(book.x)
