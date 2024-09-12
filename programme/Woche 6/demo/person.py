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