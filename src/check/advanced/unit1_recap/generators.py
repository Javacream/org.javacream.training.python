# https://realpython.com/introduction-to-python-generators/

def gen_func():
    i = 0;
    yield i
    i=i+1
    yield i
    i=i+1
    yield i

for v in gen_func():
    print(v)

#generator expression (also called a generator comprehension), 

gen = (i for i in range(1,3))
for v in gen:
    print(v)    

gen = (i for i in range(1,3))
print(gen.__next__())
print(gen.__next__())
print(gen.__next__())