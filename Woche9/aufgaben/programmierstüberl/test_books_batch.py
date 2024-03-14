import unittest
import books_batch as bb

class BooksBatchTests(unittest.TestCase):
    def test_download_books(self):
        rows = bb.download_books()
        self.assertEqual(2, len(rows))

    def test_create_sql_statements(self):
        statement1 = "INSERT INTO BOOKS (isbn, title, price, pages) VALUES ('ISBN-RUS-1', 'Title1', 19.99, 200)"
        statement2 = "INSERT INTO BOOKS (isbn, title, price, pages) VALUES ('ISBN-RUS-2', 'Title2', 9.99, 2000)"
        rows = ['Title1,19.99,200', 'Title2,9.99,2000']
        sql_statements = bb.create_sql_statements(rows)
        self.assertEqual(statement1, sql_statements[0])
        self.assertEqual(statement2, sql_statements[1])

unittest.main()