# Workaround für 'Objekte sind Unikate'
class Object:
    pass

def application():
    sawitzki = Object()
    print(sawitzki)
    print(type(sawitzki))

    sawitzki.lastname = "Sawitzki"
    sawitzki.firstname = "Rainer"
    sawitzki.height = 183

    musterfrau = Object()
    musterfrau.name = "Hannah Musterfrau"
    musterfrau.weight = 61

    person3 = Object()
    person3.lastname = "Meuer"
    person3.firstnames = ['Hugo', 'Emil'] 
    print(person3)

application()