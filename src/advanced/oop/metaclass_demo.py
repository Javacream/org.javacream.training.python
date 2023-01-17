class MyMeta(type):
    def __new__(cls, name, bases, dct):
        new_object = super().__new__(cls, name, bases, dct)
        new_object.x = "Hugo"
        return new_object
    

class Demo(metaclass=MyMeta):
    pass

d = Demo()
print(dir(d))