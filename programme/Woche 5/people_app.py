import people

def application():
    sawitzki = people.Person('Sawitzki', 'Rainer', 183) # Hier werden drei Parameter angegeben, der erste, also self wird intern erzeugt
    musterfrau = people.Person('Musterfrau', 'Hannah', 167) # Hier werden drei Parameter angegeben, der erste, also self wird intern erzeugt
    print(sawitzki.say_hello())
    print(musterfrau.say_hello())
    # print(sawitzki.__name) # Name Mangling: Private Attrib ute bekommen als öffnetlichen Namen einfach den Typen vorangestellt
    print(dir(sawitzki))
    print(sawitzki._Person__name)
application()