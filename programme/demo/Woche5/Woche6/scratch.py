class A:
    def __repr__(self):
        return f'i am {type(self)}'
    def __str__(self):
        return f'i am A'
class B(object): # Erben von (object erfolgt implizit)
    def __repr__(self):
        return f'i am {type(self)}'
    def __str__(self):
        return f'i am B'
def main():
    a = A()
    b = B()
    print(a)    
    print(b)
    objects = [a,b]
    print(objects)
if __name__ == '__main__':
    main()