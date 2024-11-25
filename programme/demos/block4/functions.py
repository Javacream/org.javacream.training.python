def function1():
    message_for_function1 = 'Hello'
    print(f'called function1, {message_for_function1}, {message}')

def function2():
    message_for_function2 = 'Goodbye'
    print(f'called function2, {message_for_function2}, {message}')
    # print(f'called function2, {message_for_function1}')

message = 'Global'
function1()
function2()
function1()
function1()



