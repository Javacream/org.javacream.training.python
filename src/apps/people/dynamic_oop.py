class Anything:
    pass

sawitzki = Anything()
#print(sawitzki)
#print(dir(sawitzki))
#print(type(sawitzki))


sawitzki.lastname = "Sawitzki"
sawitzki.firstname = "Rainer"

print(dir(sawitzki))

book = Anything()
book.isbn = "ISBN1"
book.title="Title1"

book.author = sawitzki

print(dir(book))
print(dir(book.author))