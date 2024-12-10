class A:
    def __str__(self):
        return f'i am {type(self)}'
class B(object): # Erben von (object erfolgt implizit)
    pass
def main():
    a = A()
    b = B()
    print(a)    
    print(b) 
if __name__ == '__main__':
    main()