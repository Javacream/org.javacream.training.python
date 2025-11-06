class Book:
    def __init__(self, title:str, author: str, genre: str, status=False):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

class Library:
    def __init__(self):
        self.books: set[Book] = set()

    def append(self, book: Book):
        self.books.add(book)

    def lend(book: Book):
        book.status = True

    def show(self) -> list[Book]:
        result = []
        for book in self.books:
            if book.status == False:
                result.append(book)
        return result

