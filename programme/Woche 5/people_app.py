import people

def application():
    sawitzki = people.Person('Sawitzki', 'Rainer', 183) # Hier werden drei Parameter angegeben, der erste, also self wird intern erzeugt
    musterfrau = people.Person('Musterfrau', 'Hannah', 167) # Hier werden drei Parameter angegeben, der erste, also self wird intern erzeugt
    print(sawitzki.say_hello())
    print(musterfrau.say_hello())


application()