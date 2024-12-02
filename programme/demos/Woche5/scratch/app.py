import calculator
from books import Book

def main():
    print(calculator.plus(19, 23))
    book1 = Book('ISBN1', 'Python', 19.99)
    book2 = Book('ISBN2', 'Java', 29.99)  
    print(book1.title)  
    print(type(book1))
    print(type(calculator))
    
if __name__ == '__main__':
    main()