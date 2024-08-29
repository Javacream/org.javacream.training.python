def echo(message):
    return f"echoing {message}"


def application():
    x = echo
    echoed = x("Hello") 
    print(echoed)
application()