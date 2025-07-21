def greet(name, friendly):
    if friendly:
        greeting = f'Hello {name}!'
    else:
        greeting = f'Good day {name}!'
    return greeting

print(greet('Hugo', True))
print(greet('Egon', False))