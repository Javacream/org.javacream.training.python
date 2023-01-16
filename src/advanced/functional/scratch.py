# def my_func(param1, param2):
#     print("my_func")

# my_func(1,2)

# x = my_func
# x(1,2)

# my_func = 42
# print(my_func)

# my_func(1,2)

def calc(value):
    return value * 2

#print(calc(21))

# nun: eine Art Context Manager für diese Funktion

def around(func):
    def wrapper(p):
        print("before")
        func(p)
        print("after")
    return wrapper

def stupid(func):
    return 4711


# calc = around(calc)
# calc(21)

# calc = stupid(calc)
# print(calc)

@stupid
def calc2(p):
    return 3 * p


print(calc2(14))