class Book:
    def __init__(self, title, author, genre, status) -> None:
        self:title = title
        self.author = author
        self.genre = genre
        self.status = status

class Library:
    def __init__(self) -> None:
        self.books = []
    
    def add(self, book:Book):
        self.books.append(book)
    def lend(self, book:Book)-> bool :
        if self.books.count(book) > 0:
            if (book.status == True):
                book.status = False
                return True
            else:
                return False
        else:
            return False
    def available(self) -> list:
        return [b for b in self.books if b.status == True]