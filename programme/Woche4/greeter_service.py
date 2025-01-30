def greet(name):
    greeting = f"Hello, my name is {name}"
    return greeting

if __name__ == '__main__':
    # Exemplarischer Aufruf
    demo_name = 'Hugo'
    greeting = greet(demo_name)
    print(greeting)