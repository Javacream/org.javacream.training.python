def my_func(p1, p2):
    print(p1, p2)

s = 'Foo'

# my_func is a reference, s is a reference too

s2 = s # possible? YES!, nothing new...

x = my_func # take care: NO BRACKETS, WE USE THE REFERENCE NAME, possible: YES

print(s2)
print(my_func)
my_func("Foo", "Goo") # the function will be invoked / called using brackets
x(1,2)