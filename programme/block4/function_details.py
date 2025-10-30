def do_something(dict_param):
    for key in dict_param:
        print(f'{key}={dict_param[key]}')

def do_something_with_kwargs(**dict_param):
    for key in dict_param:
        print(f'{key}={dict_param[key]}')

def main():
    person = {'name': 'Rainer Sawitzki', 'height': 183, 'weight': 75.8}
    do_something(person)
    do_something_with_kwargs(name='Rainer Sawitzki', height=183, weight=75.8)
main()