import sqlite3
import unittest

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        connection = sqlite3.connect(':memory:')  
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE BOOKS (ISBN VARCHAR(12), TITLE VARCHAR(20), PRICE DOUBLE)")
        for i in range(1, 11):
            cursor.execute(f"INSERT INTO BOOKS VALUES ('ISBN {i}', 'Title {i}', {9.99 * i})")
            self.cursor = cursor
    def tearDown(self):
        self.cursor.close()
    def test_select_all(self):
        self.cursor.execute("SELECT * FROM BOOKS")
        result = self.cursor.fetchall() 
        self.assertEqual(10, len(result))
    def test_select_by_isbn_4_has_one_result(self):
        self.cursor.execute("SELECT * FROM BOOKS WHERE ISBN = 'ISBN 4'")
        result = self.cursor.fetchall()  
        self.assertEqual(1, len(result))
    def test_select_by_isbn_42_has_no_result(self):
        self.cursor.execute("SELECT * FROM BOOKS WHERE ISBN = 'ISBN 42'")
        result = self.cursor.fetchall()  
        self.assertEqual(0, len(result))
    def test_select_by_title_like_1_has_two_results(self):
        self.cursor.execute("SELECT * FROM BOOKS WHERE TITLE LIKE '%1%'")
        result = self.cursor.fetchall()  
        self.assertEqual(2, len(result))
    def test_select_by_price_range_20_to_70_has_five_results(self):
        self.cursor.execute("SELECT * FROM BOOKS WHERE PRICE > 20 AND PRICE < 70")
        result = self.cursor.fetchall()  
        self.assertEqual(5, len(result))

if __name__ == '__main__':
    unittest.main()
