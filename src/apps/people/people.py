class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
    
    def info(self):
        return "a person: " + self.lastname + " " + self.firstname
    
    def marry(self, partner):
        if (hasattr(self, 'partner')):
            raise ValueError(self.lastname + "is married")
        if (hasattr(partner, 'partner')):
            raise ValueError(partner.lastname + "is married")
        if (self == partner):
            raise ValueError("cannot marry yourself")
        self.partner = partner
        partner.partner = self
    def divorce(self):
        if (not hasattr(self, 'partner')):
            raise ValueError(self.lastnane + "cannot divorce, is not married")
        #self.partner.partner = None
        #self.partner = None
        delattr(self.partner, 'partner')
        delattr(self, 'partner')
