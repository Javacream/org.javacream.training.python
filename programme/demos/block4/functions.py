def function1(param = 'Parameter 1'):
    for_fn1 = 'Hello'
    print(f'called function1, {for_fn1}, {param}')

def function2():
    for_fn2 = 'Goodbye'
    print(f'called function2, {for_fn2}')


def main():
    message = 'var im main-Stack'
    function1(message) # param wird mit message überschrieben, das ist unmöglich für for_fn1
    function2()

main()



