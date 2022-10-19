from random import Random


class IsbnGenerator:
    
    def __init__(self, prefix="ISBN:", suffix="-de"):
        self.generator = Random()
        self.prefix = prefix
        self.suffix = suffix
    
    
    def next_isbn(self):
        randomPart = self.generator.randint(0, 1000)
        return self.prefix + str(randomPart) + self.suffix
         
        