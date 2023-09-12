class Book:
    """A class to represent a book."""

    def __init__(self, isbn, title, price):
        """Initialize the book with an ISBN, title, and price."""
        self.isbn = isbn
        self.title = title
        self.price = price

    def get_isbn(self):
        """Return the ISBN of the book."""
        return self.isbn

    def get_title(self):
        """Return the title of the book."""
        return self.title

    def get_price(self):
        """Return the price of the book."""
        return self.price

    def set_isbn(self, isbn):
        """Set the ISBN of the book."""
        self.isbn = isbn

    def set_title(self, title):
        """Set the title of the book."""
        self.title = title

    def set_price(self, price):
        """Set the price of the book."""
        self.price = price

    def __str__(self):
        """Return a string representation of the book."""
        return f"ISBN: {self.isbn}\nTitle: {self.title}\nPrice: {self.price}"

__doc__ = """
This module contains a class to represent a book.

The Book class has methods to get and set the ISBN, title, and price of the book,
as well as a method to return a string representation of the book.
"""