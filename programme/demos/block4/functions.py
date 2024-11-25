def function1(param = 'Parameter 1'):
    for_fn1 = 'Hello'
    print(f'called function1, {for_fn1}, {param}')

def function2(param):
    for_fn2 = 'Goodbye'
    print(f'called function2, {for_fn2}, {param}')


def main():
    message = 'var im main-Stack'
    function1()
    function2(message)

main()



