class Person:
    def __getattr__(self, name):
        return name
    def __setattr__(self, name, value):
        print(name)

p = Person()
print(p.qwertzu)
setattr(p, "horst", 'hoffmann')
print(dir(p))