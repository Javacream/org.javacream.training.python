def echo(message):
    return message

def application():
    message = "Hello"
    print(echo, message)

    echoed = echo("Hello") 
    # message_result = message()
    print(echoed, message)


application()