class Book:
    def __init__(self,title:str,author:str):
        self.title = title
        self.author = author
        self.is_available = True


    def borrow(self):
        if not self.is_available:
            raise ValueError("Book is not available")
        self.is_available = False

    def return_book(self):
        if self.is_available:
            raise ValueError("The book isn't borrowed")
        self.is_available = False      

class Library:

    def __init__(self):
        self.book:list[Book] = []

    def add_book(self , book):
        self.book.append(book)

    def borrow_book(self , title : str):
        for book in self.book:
            if book.title == title:
                book.borrow()  
                return
        raise ValueError("couldn't find the book")
    def return_book(self , title : str):
        for book in self.book:
            if book.title == title:
                book.return_book()
                return
        raise ValueError("couldn't find the book")    
    
    def available_books(self) -> list[Book]:
        filtered_books = self.book(filter(book.is_available , True))
        return filtered_books
    


### Method resolution order
## Each class inherits its own method resolution order and by default the python.object, cause every single thing whatever like int ort str ... is a class 
## and the properties and the func that inherits from other classes 
    #Example:

class Horror_Book(Book):
    def __init__(self, title: str, author: str):
        super().__init__(title, author)
        self.stories:list[str] = []

### if we declare here a function like the borrow one so it's overridden on the function of the Book   
    def borrow(self):
        if not self.is_available:
            raise ValueError("this horror book is not available")
        self.is_available = True     
