def greet(name, friendly):
    if friendly:
        greeting = f'Hallo, ich bin {name}'
    else:
        greeting = f'Guten Tag, mein Name ist {name}.'
    return greeting

def main():
    test_name = 'Hugo'
    test_status = False
    greeting = greet(test_name, test_status)
    print(greeting)

main()