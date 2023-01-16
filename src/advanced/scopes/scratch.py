message = "Hello"

# globals()["m2"] = 42
# print(m2)
def f1():
    message = "World"
    print(message)

def f2():
    #globals()['message'] = "World"
    global message # anti pattern ('Sawitzki')
    message = "World"
    print(message)

def f3():
    message = "World"
    def f3_inner():
        nonlocal message
        message = "Moon"
        print(message)
    print(message)
    f3_inner()
    print(message)



print(message)
#f1()
f3()
print(message)
