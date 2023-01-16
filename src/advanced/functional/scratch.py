import functools

def trace(func):
    @functools.wraps(func)
    def wrapper_trace(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper_trace

@trace
def f1():
    return "f1"

@trace
def f2(p):
    return f"f2, p={p}"

print(f1())    
print(f2("Hugo")) 

print(f2)