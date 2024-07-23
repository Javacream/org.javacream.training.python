class AddressMixin:
    def __init__(self, address) -> None:
        self.address = address

    def normalized_address(self):
        return self.address.upper()

class TelephoneMixin:
    def __init__(self, phonenumber) -> None:
        self.phonenumber = phonenumber


class Person(AddressMixin, TelephoneMixin):
    def __init__(self, name, address, phone) -> None:
        self.name = name
        AddressMixin.__init__(self, address)
        TelephoneMixin.__init__(self, phone)

p = Person("Sawitzki", "München", "089 9999")
print(p.phonenumber)
print(p.normalized_address())
