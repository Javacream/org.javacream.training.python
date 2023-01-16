import functools

def trace(should_print):
    def decorator_trace(func):    
        @functools.wraps(func)
        def wrapper_trace(*args, **kwargs):
            if should_print:
                print("before")
            result = func(*args, **kwargs)
            print("after")
            return result
        return wrapper_trace
    return decorator_trace

@trace(True)
def f1():
    return "f1"

@trace(False)
def f2(p):
    return f"f2, p={p}"

print(f1())    
print(f2("Hugo")) 

print(f2)