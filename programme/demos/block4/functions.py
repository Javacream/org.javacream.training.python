def function1():
    global message
    for_fn1 = 'Hello'
    message = 'Global, changed by fn1'
    print(f'called function1, {for_fn1}, {message}')

def function2():
    for_fn2 = 'Goodbye'
    print(f'called function2, {for_fn2}, {message}')
    #print(f'called function2, {for_fn1}')

message = 'Global'
function1()
function2()
function1()
function1()



