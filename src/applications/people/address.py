class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street
    def info(self):
        return f'Address(city={self.city}, street={self.street})'