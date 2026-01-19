def my_func():
    print('my_func, no param')
def my_func(p):
    print(f'my_func, one param {p}')

def main():
    # my_func() # my_func wurde durch die neue Definition mit einer Funktion mit einem Parameter ersetzt
    my_func('Hugo')

main()