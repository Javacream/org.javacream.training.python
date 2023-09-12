class Book:
    str_template = 'Book: isbn={}, title={}, price={}'
    def __init__(self, isbn, title, price):
        self.isbn = isbn
        self.title = title
        self.price = price
    def __str__(self):
        return Book.str_template.format(self.isbn, self.title, self.price)


class BooksManager:
    def __init__(self, books = dict()):
        self.books = books

    def books_with_title_containing_python(self):
        books_list = self.books.values()
        return [book for book in books_list if 'Python' in book.title]

    def books_with_price_greater_than_50(self):
        books_list = self.books.values()
        return [book for book in books_list if book.price >= 50]
    def average_book_price(self):
        books_list = self.books.values()
        price_sum = 0
        for book in books_list:
            price_sum += book.price
        return price_sum / len(books_list)
    def books_with_shortest_and_longest_title(self):
        books_list = self.books.values()
        shortest = 100000
        longest = 0
        for book in books_list:
            title_length = len(book.title)
            if  title_length < shortest:
                shortest = title_length
            if title_length > longest:
                longest = title_length
        shortes_books = [b for b in self.books.values() if len(b.title) == shortest] 
        longest_books = [b for b in self.books.values() if len(b.title) == longest] 

        return (shortes_books, longest_books)