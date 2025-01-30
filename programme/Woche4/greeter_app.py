import greeter_service as greeter
def main():
    name = input('Bitte Name eingeben: ')
    greeting = greeter.greet(name)
    print(greeting)

if __name__ == '__main__':
    main()

