def no_param_function():
    print('a parameterless function')

def one_param_function(param):
    print(f'one parameter {param} function')

def one_default_param_function(param = 'Egon'):
    print(f'one parameter {param} function')

def one_param_and_one_default_param_function(p1, p2 = 'Egon'):
    print(f'first parameter {p1}, second {p2} function')

#def wrong_syntax(p1, p2 = 'Egon', p3):
#    pass

def main():
    no_param_function()
    # no_param_function('Hugo')
    one_param_function('Hugo')
    # one_param_function()
    # one_param_function('Hugo', 'Hannah')
    one_default_param_function('Hugo')
    one_default_param_function()
    one_param_and_one_default_param_function(42)
    one_param_and_one_default_param_function(42, 'Hannah')



main()