class Person:
    def __init__(self, username, id, firstname, lastname, active):
        self.username = username    
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.active = True if active == 'active' else False
    def __repr__(self) -> str:
        return f'username={self.username}, id={self.id}, firstname={self.firstname}, lastname={self.lastname}'    
    def __add__(self, other):
        return Person(self.username + other.username, self.id - other.id, "EG", "AL", 'inactive')
p1 = Person("mei", 12345, "Meier", "Hannah", "active")
p2 = Person("sawi", 666, "Sawitzki", "Rainer", "active")

p3 = p1 + p2
print(p3)