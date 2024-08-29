def f1(p_f1):
    global global_message
    global_message = "CHANGED"
    number = 42
    print(p_f1)
    f2(number)
    print(global_message)

def f2(p_f2):
    state = True
    name = 'Sawitzki'
    print(p_f2)
    print(global_message)    

global_message = 'Global Hello'
message = "Hello"

f1(message)