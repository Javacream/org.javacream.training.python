message = 'Hello'
message2 = 'Emil'
def fn1():
    print(message)
    print(message2)
def main():
    message = 'Goodbye' # hier wird einfach eine lokale Variable angelegt, die die globale überschattet
    global message2
    message2='Hugo'
    fn1()

main()