def greet(name, status):
    if status == 'friendly':
        greeting = f'Hallo, ich bin {name}'
    elif status == "formal":
        greeting = f'Guten Tag, mein Name ist {name}.'
    else:
        greeting = name    
    return greeting

def main():
    test_name = 'Hugo'
    test_status = 'formal'
    greeting = greet(test_name, test_status)
    print(greeting)

main()