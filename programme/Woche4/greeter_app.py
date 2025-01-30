import greeter_service

def main():
    name = input('Bitte Name eingeben: ')
    greeting = greeter_service.greet(name)
    print(greeting)

if __name__ == '__main__':
    main()

