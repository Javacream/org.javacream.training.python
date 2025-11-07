import sys
sys.path.append('./programme/block5')
from library import Library, Book
from people.people import Person
def main():
    library = Library()
    b1 = Book('Python', Person('Writer', 'John', 188, 77.7), 'computer languages')
    library.append(b1)
    b2 = Book('A romance in yellow', Person('Au', 'Thor', 138, 47.7), 'novelle')
    library.append(b2)

    print(b1.status, b2.status)
    library.lend(b2)
    print(b1.status, b2.status)

    print(library.show())

main()