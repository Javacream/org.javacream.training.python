def my_function():
    print(f'my_function has no params')
def my_function(p):
    print(f'my_function has one param')
def function_with_default_values(p1='Hugo', p2=True):
    print(f'function_with_default_values, param1={p1}, param2={p2}')
def function_with_varargs(*args):
    for param in args:
        print(param)
def function_with_keyworded_args(**kwargs):
    for key in kwargs:
        print(f'{key}={kwargs[key]}')


def main():
    # my_function() # my_function without param was redefined / overwritten in line 3
    my_function('Hugo')
    function_with_default_values()
    function_with_default_values(42)
    function_with_default_values('Emil', 42)
    function_with_varargs()
    function_with_varargs(1)
    function_with_varargs(1,2)
    function_with_keyworded_args()
    function_with_keyworded_args(this='that')
    function_with_keyworded_args(name='Hugo', weight=76.8)


main()

