from greeter_service import greet
def main():
    name = input('Bitte Name eingeben: ')
    greeting = greet(name)
    print(greeting)

if __name__ == '__main__':
    main()

