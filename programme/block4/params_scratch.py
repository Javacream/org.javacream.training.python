def one_param(p):
    print(f'param={p}')

def one_default_param(p='Emil'):
    print(f'param={p}')

def default_params(p1='Emil', p2=4711):
    print(f'params={p1}, {p2}')
def param_and_default_params(p, p1='Emil', p2=4711):
    print(f'params={p}, {p1}, {p2}')

#def wrong_param_and_default_params(p1='Emil', p, p2=4711):
#    print(f'params={p}, {p1}, {p2}')

def main():
    value = 'Hugo'
    one_param(value)
    # one_param()
    # one_param(value, 42)
    one_default_param(value)
    one_default_param()
    # one_default_param(value, 42)
    default_params()
    default_params(value)
    default_params(value, 42)

    # param_and_default_params()
    param_and_default_params(value)
    param_and_default_params(value, 42)
    param_and_default_params(value, 42, True)
main()