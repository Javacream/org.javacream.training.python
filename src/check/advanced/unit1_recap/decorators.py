#https://realpython.com/primer-on-python-decorators/

def step1(param):
    print(param)
    def f(func):
        return param
    return f

@step1("Hugo")
def demo():
    return 4711

print(demo)