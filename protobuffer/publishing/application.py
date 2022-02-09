from book_pb2 import Book
from google.protobuf.json_format import MessageToJson

book = Book()
book.isbn = 'Isbn1'
book.title = 'Title1'
book.price = 19.99
#book.preis = 19.99 # geht nicht!
#book.price = "19.99" # geht nicht!

book.pages = 200
book.available = True
book.tags.append("sports")
book.tags.append("politics")
print(book)

with open("book.bin", "wb") as f:
    print("write as binary")
    bytesAsString = book.SerializeToString()
    f.write(bytesAsString)


with open("book.bin", "rb") as f:
    print("read values")
    book_read = Book().FromString(f.read())


print(book_read)


print("Is Available?: " + str(book_read.available))
print("Isbn?: " + str(book_read.isbn))
print("Tags?: " + str(book_read.tags))

json_book = MessageToJson(book)
print(json_book)