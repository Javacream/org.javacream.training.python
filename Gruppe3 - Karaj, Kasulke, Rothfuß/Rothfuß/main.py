"""
This script imports a list of books from a CSV file, stores them in a BookManager object,
and then queries the object for various information.

The CSV file should have the following format:
Title, Author, Price
Book 1, Author 1, 10.99
Book 2, Author 2, 29.99
...

The script imports the Book and BookManager classes from the book.py 
and bookmanager.py files, respectively.

The script defines a my_price_func function that takes a Book object and a price argument 
and returns True if the book's price is greater than the price argument, and False otherwise.

The script opens the books.csv file and reads it line by line. It creates a Book object 
for each line using the data from the CSV file, adds the Book object to the BookManager object,
and then prints the books in the BookManager object.

The script then queries the BookManager object for books with a given title, 
books with a given price, the average price of all books, books with the shortest titles, 
and books with the longest titles. It prints the results of each query.

Note: The script assumes that the CSV file is in the same directory as the script 
and that the Book and BookManager classes are in the same directory as the script.
"""

import book as bk
import bookmanager as bkm

my_bkm = bkm.BookManager()

def my_price_func(b_k, price):
    """Returns True if the book's price is greater than the price argument, and False otherwise."""
    return int(b_k.price) > price

with open("books.csv", mode="r", encoding="utf-8") as file:
    next(file)
    for row in file:
        if row.endswith('\n'):
            row = row[0:len(row)-1]
        data = row.split(",")

        my_book = bk.Book(data[0], data[1], data[2])

        my_bkm.add_book(my_book)

print("Number of books: " + str(my_bkm.get_number_of_books()))

print("All books: ")
my_bkm.print_books()

bkm_dupe, bkm_unique = my_bkm.get_books_with_same_isbn()
print("Dupe books:")
print("Number of dupe books: " + str(bkm_dupe.get_number_of_books()))
bkm_dupe.write_books_to_file("books_with_same_isbn.csv")
bkm_dupe.print_books()
print("Unique books:")
print("Number of unique books: " + str(bkm_unique.get_number_of_books()))
bkm_unique.write_books_to_file("books_with_unique_isbn_.csv")
bkm_unique.print_books()

print("Books whose title contains: Python")
book_list = my_bkm.get_books_by_title("Python")
bkm_python = bkm.BookManager()
for book in book_list:
    print(book)
    bkm_python.add_book(book)
bkm_python.write_books_to_file("books_with_title_python.csv")

print("Books whose price is: Greater than 50")
book_list = bkm_unique.get_books_by_price(my_price_func, 50)
bkm_prize_50 = bkm.BookManager()
for book in book_list:
    print(book)
    bkm_prize_50.add_book(book)
bkm_prize_50.write_books_to_file("books_with_price_greater_than_50.csv")

AVG_BOOK_PRICE = str(bkm_unique.get_average_price())
print("Average price: " + AVG_BOOK_PRICE)
with open("average_book_price.txt", mode="w", encoding="utf-8") as file:
    file.write(AVG_BOOK_PRICE)

print("Books with the shortest titles")
book_list = bkm_unique.get_shortest_titles()
bkm_short_titles = bkm.BookManager()
for book in book_list:
    print(book)
    bkm_short_titles.add_book(book)
bkm_short_titles.write_books_to_file("books_with_shortest_titles.csv")

print("Books with the longest titles")
book_list = bkm_unique.get_longest_titles()
bkm_longest_titles = bkm.BookManager()
for book in book_list:
    print(book)
    bkm_longest_titles.add_book(book)
bkm_longest_titles.write_books_to_file("books_with_longest_titles.csv")
