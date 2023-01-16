class SimpleIterator:
    def __iter__(self):
        print("initializing")
        return self
    def __next__(self):
        print ("next")
        raise StopIteration    
    

si = SimpleIterator()
for v in si:
  print(v)