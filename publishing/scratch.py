import pickle

class Publisher:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        self.books = set()

p = Publisher(1, "Springer", "München")
p.books.add("Book1")
p.books.add("Book2")
p.books.add("Book3")

#serializedPublisher = pickle.dumps(p)
#print(serializedPublisher)

with open("publisher.pickle", 'wb') as file:
    pickle.dump(p, file)

with open("publisher.pickle", 'rb') as file:
    loaded = pickle.load(file)
    print(type(loaded))
    print(loaded.books)
