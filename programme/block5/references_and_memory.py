def my_function(names_list, text, n):
   # names_list.append('Andrea')
    names_list = ['Andrea']
    text ='CHANGED'
    n = 42
    print(f'In my_function: Names: {names_list}, text={text}, n={n}')

def main():
    message = 'Hello'
    number = 9
    names = ['Hugo', 'Emil', 'Hannah']
    my_function(names, message, number) # implizit: names_list = names, text = message, n number
    print(f'In main: Names {names}, message={message}, number={number}')

main()