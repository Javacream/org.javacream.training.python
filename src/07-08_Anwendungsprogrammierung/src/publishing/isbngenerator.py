from random import Random
import sys


class IsbnGenerator(object):
    
    def __init__(self, prefix="ISBN:", suffix="-de"):
        '''
        >>> generator = IsbnGenerator()
        >>> generator.next_isbn().startswith("ISBN:")
        True
        >>> generator.next_isbn().endswith("-de")
        True
        '''
        self.generator = Random()
        self.prefix = prefix
        self.suffix = suffix
    
    
    def next_isbn(self):
        '''Generates an unique ISBN number
        >>> generator = IsbnGenerator()
        >>> generator.prefix="TEST"
        >>> generator.suffix="-dk"
        >>> generator.next_isbn().startswith("TEST")
        True
        >>> generator.next_isbn().endswith("-dk")
        True
        '''
        randomPart = self.generator.randint(0, sys.maxsize)
        return self.prefix + str(randomPart) + self.suffix
         
        