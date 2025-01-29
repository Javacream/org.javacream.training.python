def greet(name):
    greeting = f'Hallo, ich bin {name}'
    return greeting

def main():
    test_name = 'Hugo'
    greeting = greet(test_name)
    print(greeting)

main()