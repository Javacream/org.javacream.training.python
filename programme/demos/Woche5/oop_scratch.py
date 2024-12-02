l1 = list()
l2 = list()

print(type(l1), type(l2))

l1.append('Hugo')
l2.append('Waldo')
l2.append('Hannah')

print(l1[0])
print(l2[0])

class Empty:
    pass

instance_of_empty1 = Empty()
instance_of_empty2 = Empty()

print(type(instance_of_empty1), type(instance_of_empty2))

instance_of_empty1.lastname = "Sawitzki"
instance_of_empty2.name = "Andrea Musterperson"
instance_of_empty1.firstname = ["Rainer", "Ulrich"]

print(instance_of_empty1.lastname)
print(instance_of_empty2.name)

# l1.name = 'Meine spezielle Liste' -> Bestimmte Objekte sind nicht dynamisch, können nicht erweitert werden





