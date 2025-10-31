def fn1():
    global message
    message = 'CHANGED'
    print(message)

def main():
    fn1()
    print(message)

message = 'global var'
main()