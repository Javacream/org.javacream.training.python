class Demo:
    def __init__(self, public, private):
        self.public = public
        self.__private = private

def main():
    d = Demo("pub", "secret")
    print(d.public)
    print(d._Demo__private)

if __name__=='__main__':
    main()