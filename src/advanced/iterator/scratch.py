r = range(1,4)

for element in r:
    print(element)


class SimpleIterator:
    def __iter__(self):
        print("initializing")    
        return self
    def __next__(self):
        print("next")
        raise StopIteration

for element in SimpleIterator():
    print(f"Element: {element}")