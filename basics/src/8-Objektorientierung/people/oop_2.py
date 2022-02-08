class Any:
    pass

a_person = Any()
#print(a_person)
#print(dir(a_person))
#print(type(a_person))

a_person.id=42
a_person.lastname = "Meier"
a_person.firstname = "Hugo"

#print(dir(a_person))

munich = Any()
munich.street="Marienplatz"
munich.city = "munich"

a_person.address = munich

print(a_person.address.city)
