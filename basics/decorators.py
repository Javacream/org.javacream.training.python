def say_hello():
    print('Hello')

def say_goodbye():
    print('Goodbye')


say_hello()
say_goodbye()    

# ToDo: Sowohl say_hello als auch say_goodbye mögen bitte zwei zusätzliche Ausgaben enthalten, 'entering', 'exiting'

def trace(fn):
    def decorator():
        print("entering")
        fn()
        print("exiting")
    return decorator

say_hello = trace(say_hello)    
say_goodbye = trace(say_goodbye)

say_hello()
say_goodbye()

@trace # in anderen Sprachen wird soetwas als eine Annotation bezeichnet
def should_be_decorated():
    print('HUGO')

should_be_decorated()
