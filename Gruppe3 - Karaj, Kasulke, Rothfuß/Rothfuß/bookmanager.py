class BookManager:
    """
    This class is responsible for managing a collection of books.
    """

    def __init__(self):
        self.books = []

    def get_number_of_books(self):
        """
        Returns the number of books in the collection.
        """
        return len(self.books)

    def add_book(self, book):
        """
        Adds a book to the collection.

        Args:
            book (Book): The book to add.
        """
        self.books.append(book)

    def get_books(self):
        """
        Returns a list of all books in the collection.

        Returns:
            list: A list of all books.
        """
        return self.books

    def get_book(self, book):
        """
        Returns a specific book from the collection.

        Args:
            book (Book): The book to retrieve.

        Returns:
            Book: The requested book, or None if it does not exist.
        """
        for b_k in self.books:
            if b_k.title == book.title:
                return b_k
        return None

    def update_book(self, book):
        """
        Updates a book in the collection.

        Args:
            book (Book): The book to update.

        Returns:
            bool: True if the book was updated, False if it did not exist.
        """
        for b_k in self.books:
            if b_k.title == book.title:
                b_k.title = book.title
                b_k.author = book.author
                b_k.publisher = book.publisher
                b_k.year = book.year
                b_k.pages = book.pages
                b_k.price = book.price
                return True
        return False

    def search_book(self, book):
        """
        Searches for a book in the collection.

        Args:
            book (Book): The book to search for.

        Returns:
            Book: The requested book, or None if it does not exist.
        """
        for b_k in self.books:
            if b_k.title == book.title:
                return b_k
        return None

    def print_books(self):
        """
        Prints a list of all books in the collection.
        """
        for b_k in self.books:
            print(f"ISBN: {b_k.isbn}, Title: {b_k.title}, Price: {b_k.price}")

    def get_books_by_title(self, title):
        """
        Returns a list of all books in the collection that have the given title.

        Args:
        title (str): The title to search for.
        """
        return [b_k for b_k in self.books if title in b_k.title]

    def get_books_by_price(self, price_func, price):
        """
        Returns a list of all books in the collection that match the given price function.

        Args:
        price_func: The price function to match.
        """
        return [b_k for b_k in self.books if price_func(b_k, price)]

    def get_average_price(self):
        """
        Returns the average price of all books in the collection.
        """
        return sum([int(b_k.price) for b_k in self.books]) / len(self.books)

    def get_longest_titles(self):
        """
        Returns the longest title of all books in the collection.
        """
        title_len = max([len(b_k.title) for b_k in self.books])

        return [b_k for b_k in self.books if len(b_k.title) == title_len]


    def get_shortest_titles(self):
        """
        Returns the longest title of all books in the collection.
        """
        title_len = min([len(b_k.title) for b_k in self.books])

        return [b_k for b_k in self.books if len(b_k.title) == title_len]

    def get_books_with_same_isbn(self):
        """
        Get all books that have the same ISBN.
        """
        isbn_list = []
        for b_k in self.books:
            isbn_list.append(b_k.isbn)

        isbn_list_dupes = set([x for x in isbn_list if isbn_list.count(x) > 1])
        isbn_list_unique = set([x for x in isbn_list if isbn_list.count(x) == 1])

        bkm_dupe = BookManager()
        bkm_unique = BookManager()

        for b_k in self.books:
            if b_k.isbn in isbn_list_dupes:
                bkm_dupe.add_book(b_k)
            elif b_k.isbn in isbn_list_unique:
                bkm_unique.add_book(b_k)

        return bkm_dupe, bkm_unique

    def write_books_to_file(self, file_name):
        """
        Writes all books in the collection to a file.
        """
        with open(file_name, mode="w", encoding="utf-8") as file:
            for b_k in self.books:
                file.write(f"{b_k.isbn},{b_k.title},{b_k.price}\n")

__doc__ = """
This module contains the BookManager class.

The BookManager class is responsible for managing a collection of books. It provides methods for adding, deleting, updating, searching for, and printing books.
"""