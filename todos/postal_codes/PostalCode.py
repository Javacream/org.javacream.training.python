import csv
class PostalCode:
    def __init__(self, city, postal_code, district):
        self.city = city
        self.postal_code = postal_code
        self.district = district
    def __repr__(self):
        return f"PostalCode: city={self.city}, code={self.postal_code}, district={self.district}"    

def read_data():
    with open ('german-postcodes.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=';')
        next(csv_reader)  # Erste Zeile als Header lesen und ignorieren
        data = [PostalCode(row[0], row[1], row[2]) for row in csv_reader]
        return data
