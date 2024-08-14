def say_hello():
    print('Hello')

def say_goodbye():
    print('Goodbye')


say_hello()
say_goodbye()    

# ToDo: Sowohl say_hello als auch say_goodbye mögen bitte zwei zusätzliche Ausgaben enthalten, 'entering', 'exiting'

def trace(detail):
    def inner(fn):
        def decorator(*args, **kwargs):
            if detail:
                print(f"entering using {args} {kwargs}")
            else:
                print(f"entering")    
            result = fn(*args, **kwargs)
            if detail:
                print(f"exiting retrieving {result}")
            else:
                print(f"exiting")    
            return result
        return decorator
    return inner
#say_hello = trace(say_hello, False)    
#say_goodbye = trace(say_goodbye, True)

say_hello()
say_goodbye()

@trace(detail=True) # in anderen Sprachen wird soetwas als eine Annotation bezeichnet
def should_be_decorated(mult):
    return mult * 'HUGO'

print (should_be_decorated(3))
