import people

def application():
    sawitzki = people.Person('Sawitzki', 'Rainer', 183, people.Address('München', 'Marienplatz')) 
    musterfrau = people.Person('Musterfrau', 'Hannah', 167, people.Address('Berlin', 'Alexanderplatz'))
    print(sawitzki.say_hello())
    sawitzki.addresses.append(people.Address('Frankfurt', 'Niederrad'))
    einstein = people.Student("Einstein", 'Albert', 166, None, "LMU")
    print(einstein.say_hello())    
application()