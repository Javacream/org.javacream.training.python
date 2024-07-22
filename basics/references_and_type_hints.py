def string_demo(p:str):
    print(p)

def string_demo_reassignement(p:str):
    p = "Goodbye"
    print(p)

def string_demo_change_object(p:str):
    # Wie kann denn ein String geändert werden -> MISSION IMPOSSIBLE!
    print(p)


def list_demo(p:list):
    p.append("Egon") # wird zu einem Fehler führen, wenn p gar keine Liste isr
    print(p)

def list_demo_reassignement(p:list):
    p = []
    p.append("Egon")
    print(p)

def list_demo_change_object(p:list):
    p.append("Egon")
    print(p)


def main():
    message = "Hello"
    names = ["Hugo", "Emil"]
    list_demo(names)
    # list_demo(message) # dieser fehlerhafte Aufruf ist möglich trotz type hint in list_demo!
    list_demo_reassignement(names)
    print(names) # Ein reassignement in der Funktion führt zu einem Umbiegen der Referenz, das Original deutet woanders hin
    list_demo_change_object(names)
    print(names) # Nachdem wir in OOP ein "copy value of reference" haben wird auch die originale Referenz auf das ursprüngliche Objekt verweisen und damit die Änderung anzeigen

    string_demo_reassignement(message) # Analog zu list_demo_ressignement

    l1 = [1]
    l2 = l1.copy()
    l2.append(42)
    print(l1)

    print(type(l1))

main()
