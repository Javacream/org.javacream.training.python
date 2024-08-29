def echo(message:str, prefix):
    if prefix:
        return "Echoed " + message
    else:
        return message

def echo(message):
    return f"echoing {message}"


def application():
    echoed = echo("Hello", False) 
    echo("Hello")
    print(echoed)
application()