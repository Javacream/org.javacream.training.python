def dec(cls):
    class Decorated(cls):
        x = "Hugo"
    return Decorated    

@dec
class Demo():
    pass

print(dir(Demo))