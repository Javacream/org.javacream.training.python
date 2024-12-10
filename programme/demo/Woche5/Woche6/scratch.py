def complex_oop(obj):
    print('entering')
    print(obj.info())
    print('exiting')

class A:
    def info(self):
        return "i am A"    
class B:
    def info(self):
        return "i am B"    

def main():
    a = A()
    b = B()
    complex_oop(a)
    complex_oop(b)

if __name__ == '__main__':
    main()