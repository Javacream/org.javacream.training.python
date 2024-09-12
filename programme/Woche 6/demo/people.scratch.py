class Person:
    def __init__(self, username, id, firstname, lastname, active):
        self.username = username    
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.active = True if active == 'active' else False
    def __repr__(self) -> str:
        return f'username={self.username}, id={self.id}, firstname={self.firstname}, lastname={self.lastname}'    
    def __eq__(self, other) -> bool:
        return self.id == other.id
    def __hash__(self) -> int:
        return hash(self.id)

p1 = Person("mei", 12345, "Meier", "Hannah", "active")
p2 = Person("sawi", 666, "Sawitzki", "Rainer", "active")
p3 = Person("mei", 12345, "Meier", "Hannah", "active")

addresses = dict()
addresses[p1] = "Berlin"
addresses[p2] = "München"

print(p1 == p3)
print(addresses.get(p1))
print(addresses.get(p3))
