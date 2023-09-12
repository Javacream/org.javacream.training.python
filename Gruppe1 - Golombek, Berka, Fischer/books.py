class Book:
    def __init__(self, ISBN, title, price):
        self.ISBN = ISBN
        self.title = title
        self.price = float(price)
    def title_length(self):
        return len(self.title)
        
        
class BookManager:
    def __init__(self, filename):
        self.books = {}
        self.counter = 0
        self.filename = filename
        self.__load_books__(filename)
    def create(self, ISBN, title, price):
        self.counter += 1
        new_book = Book(ISBN, title, price)
        self.books[self.counter] = new_book
    def __load_books__(self, filename):
        self.filename = filename
        with open(filename, "r", encoding="utf-8") as file:
            input_str = file.read()
            input_list = input_str.split("\n")
            input_list.pop(0)
            for element in input_list:
                data = element.split(",")
                self.create(*data)
    def find_duplicate_isbn(self):
        list_of_duplicate_isbns = set()
        list_of_checked_isbns = set()
        for key, value in self.books.items():
            if value.ISBN not in list_of_checked_isbns:
                list_of_checked_isbns.add(value.ISBN)
            else: 
                list_of_duplicate_isbns.add(value.ISBN)
        return list_of_duplicate_isbns
    def find_by_ISBN(self, ISBN):
        return [key for key in self.books.keys() if self.books.get(key).ISBN == ISBN]
    def find_by_title(self, name):
        return [books for books in self.books.values() if name in books.title]
    def find_by_price(self, min_price):
        return [books for books in self.books.values() if books.price > min_price]
    def find_by_title_length(self, length):
        return [books for books in self.books.values() if books.title_length() == length]