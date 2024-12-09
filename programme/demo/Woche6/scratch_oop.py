class Anything(object):
    def __str__(self):
        return 'anything'    
def main():
    obj = Anything()
    obj2 = object()
    print(obj, obj2)    

if __name__ == '__main__':
    main()    