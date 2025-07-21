def greet(name, friendly):
    if friendly:
        greeting = f'Hello {name}!'
    else:
        greeting = f'Good day {name}!'
    return greeting

def main():
    print(greet('Hugo', True))
    name = 'Egon'
    greeting_cat = False
    greeting = greet(name, greeting_cat)
    print(greeting)

main()