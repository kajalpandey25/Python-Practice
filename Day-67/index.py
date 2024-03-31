class Library:
    def __init__(self):
        self.noBooks = 0 
        self.books = []

    def addBooks(self, book):
        self.books.append(book) 
        self.noBooks =   len(self.books)

    def showInfo(self):
        print(f"The library has {self.noBooks} books. The books are: ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBooks("Kajal Potter")
l1.addBooks("Go with the flow")
l1.addBooks("One night")
l1.showInfo()         