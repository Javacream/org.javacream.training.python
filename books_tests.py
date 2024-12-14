import unittest
from book import Book
import books_service
class BookTests(unittest.TestCase):
    def test_book_construction(self):
        isbn = 42
        title = 'Book-Title'
        price = 9.99
        pages = 200
        available = True
        book = Book(isbn, title, price, pages, available)
        self.assertEqual(isbn, book.isbn)
        self.assertEqual(title, book.title)
        self.assertEqual(price, book.price)
        self.assertEqual(pages, book.pages)
        self.assertEqual(available, book.available)
    def test_book_representation(self):
        book = Book(42, 'Book-Title', 9.99, 200, True)
        expected_repr = 'Book: isbn=42, title=Book-Title, price=9.99, pages=200, available=True'
        self.assertEqual(expected_repr, repr(book))
    def test_book_equality(self):
        book1 = Book(42, 'Book-Title', 9.99, 200, True)
        book2 = Book(42, 'XYZ', 9.99, 200, True)
        book3 = Book(666, 'XYZ', 9.99, 200, True)
        self.assertEqual(book1, book2)
        self.assertNotEqual(book1, book3)
        self.assertEqual(hash(book1), hash(book2))
        self.assertNotEqual(hash(book1), hash(book3))

class BooksServiceTests(unittest.TestCase):
    def test_valid_params_create_a_book(self):
        title = 'Book-Title'
        price = 9.99
        pages = 200
        available = True
        isbn = books_service.create(title, price, pages, available)
        self.assertIsNotNone(isbn)
    def test_invalid_price_raises_exception(self):
        title = 'Book-Title'
        price = -1
        pages = 200
        available = True
        try:
            books_service.create(title, price, pages, available)
            self.fail()
        except Exception as e:
            self.assertEqual('invalid price, must be greater or equal 0, was -1', str(e))    
    def test_invalid_pages_raises_exception(self):
        title = 'Book-Title'
        price = 1
        pages = 0
        available = True
        try:
            books_service.create(title, price, pages, available)
            self.fail()
        except Exception as e:
            self.assertEqual('invalid page count, must be greater than 0, was 0', str(e))    
    def test_created_books_are_stored(self):
        books_service.books.clear()
        books_service.create('Title1', 9.99, 200, True)
        self.assertEqual(1, len(books_service.find_all()))
        books_service.create('Title2', 9.99, 200, True)
        self.assertEqual(2, len(books_service.find_all()))
        books_service.create('Title3', 9.99, 200, True)
        self.assertEqual(3, len(books_service.find_all()))

    def test_contained_isbn_is_found(self):
        TEST_ISBN = 1
        test_book = Book(TEST_ISBN, 'Title', 9.99, 200, True)
        books_service.books = {TEST_ISBN: test_book}
        self.assertEqual(test_book, books_service.find_by_isbn(TEST_ISBN))

    def test_unknown_isbn_finds_None(self):
        books_service.books.clear()
        UNKNOWN_ISBN = 42
        self.assertIsNone(books_service.find_by_isbn(UNKNOWN_ISBN))

    def test_contained_isbn_can_be_deleted(self):
        TEST_ISBN = 1
        test_book = Book(TEST_ISBN, 'Title', 9.99, 200, True)
        books_service.books = {TEST_ISBN: test_book}
        self.assertTrue(books_service.delete_by(TEST_ISBN))
        self.assertFalse(books_service.delete_by(TEST_ISBN))

    def test_unknown_isbn_cannot_be_deleted(self):
        books_service.books.clear()
        UNKNOWN_ISBN = 42
        self.assertFalse(books_service.delete_by(UNKNOWN_ISBN))
    def test_find_by_title_finds_two_python_books(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 9.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 9.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(2, len(books_service.find_by_title('Python')))
    def test_find_by_title_finds_one_java_book(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 9.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 9.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(1, len(books_service.find_by_title('Java')))
    def test_find_by_title_finds_no_javascript_book(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 9.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 9.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(0, len(books_service.find_by_title('JavaScript')))
    def test_find_by_price_range_no_params_finds_all(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 19.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 29.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(3, len(books_service.find_by_price_range()))
    def test_find_by_price_range_min_price_10_finds_two_books(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 19.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 29.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(2, len(books_service.find_by_price_range(10)))
    def test_find_by_price_range_min_price_20_finds_one_book(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 19.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 29.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(1, len(books_service.find_by_price_range(20)))
    def test_find_by_price_range_min_price_30_finds_no_book(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 19.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 29.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(0, len(books_service.find_by_price_range(30)))
    def test_find_by_price_range_min_price_10_and_max_price_20_finds_one_book(self):
        books_data = {
            1: Book(1, 'Python in Action', 9.99, 200, True),
            2: Book(2, 'A Java Action', 19.99, 200, True),
            3: Book(3, 'Grundlagen: Python, PERL', 29.99, 200, True)
            }
        books_service.books = books_data
        self.assertEqual(1, len(books_service.find_by_price_range(10, 20)))

if __name__ == '__main__':
    unittest.main()