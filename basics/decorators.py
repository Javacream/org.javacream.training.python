def say_hello():
    print('Hello')

def say_goodbye():
    print('Goodbye')


say_hello()
say_goodbye()    

# ToDo: Sowohl say_hello als auch say_goodbye mögen bitte zwei zusätzliche Ausgaben enthalten, 'entering', 'exiting'

def decorate(fn):
    def decorator():
        print("entering")
        fn()
        print("exiting")
    return decorator

say_hello = decorate(say_hello)    
say_goodbye = decorate(say_goodbye)

say_hello()
say_goodbye()    

