class SimpleList(object):
    def __init__(self, size):
        self.size = size
        self.position = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.position < self.size:
            self.position = self.position + 1
            return self.position
        else:
            raise StopIteration()

simple_list = SimpleList(5)
for i in simple_list:
    print(i)

# Entsprechung als generator-Funktion

def simple_iteration(size):
    position = -1
    if position < size:
        position = position + 1
        yield position
  