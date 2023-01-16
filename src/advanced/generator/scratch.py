def generator_function():
    yield "Hugo"
    yield 42
    yield True

for element in generator_function():
    print(element)


generator = (i for i in range(1,3))

for e in generator:
    print(e)

generator = (i for i in range(1,3))

print(generator.__next__())
