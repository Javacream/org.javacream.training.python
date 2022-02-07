counter = 0
def create_person(lastname, firstname):
    global counter
    counter = counter + 1
    return (counter, lastname, firstname)

p1 = create_person("Sawitzki", "Rainer")
p2 = create_person("Sawitzki", "Hanna")
p3 = create_person("Metzger", "Georg")

s = {p1, p2, p3, p1, p2}
l = [p1, p2, p3, p1, p2]
d = {p1[0]:p1, p2[0]:p2, p3[0]:p3}

print(s)
print(l)
print(d)



