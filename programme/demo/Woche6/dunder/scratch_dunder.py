class Anything:
    def info(self):
        print('info')
    def __repr__(self):
        return 'repr anything'
    def __str__(self):
        return 'str anything'
    
def main():
    a = Anything()
    print(repr(a))    
    print(a.__repr__()) 
    print(str(a))    
    print(a.__str__()) 
    print(dir(a))    
    print(a.__dir__()) 

if __name__ == '__main__':
    main()       
