def greet(p1):
    welcome = "Hello"
    greeting = welcome + " " + p1 + "!"
    print(greeting)
    return_value = "OK"
    return return_value

def main():
    name = "Hugo"
    greet_result = greet(name)
    print(greet_result)

def something(): # definiert, aber nie aufgerufen
    print("doing something") 

main()