import mysql.connector 
class Book:
    def __init__(self, book_data: tuple):
        self.isbn: str = book_data[0]
        self.title: str = book_data[1]
        self.price: float = book_data[2]
        self.available: bool = book_data[3]
    def __repr__(self):
        return f'Book(isbn={self.isbn}, title={self.title}, price={self.price}, available={self.available})'
class BooksService:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='javacream.eu', 
            port=3406,
            database='javacream',
            user = 'user',
            password='user')
        self.cursor = self.connection.cursor()
    def search_by(self, isbn: str) -> Book:
        sql = f"SELECT * FROM BOOKS WHERE ISBN = '{isbn}'"
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        book = Book(data)
        return book
    def find_all(self) -> list[Book]:
        sql = f"SELECT * FROM BOOKS"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        return [Book(data) for data in datas]
