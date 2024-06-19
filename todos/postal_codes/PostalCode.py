class PostalCode:
    def __init__(self, city, postal_code, district):
        self.city = city
        self.postal_code = postal_code
        self.district = district
    def __repr__(self):
        return f"PostalCode: city={self.city}, code={self.postal_code}, district={self.district}"    

def read_data():
    print("reading data")
    with open ('german-postcodes.csv', 'r', encoding='utf-8') as file:
        raw_data =  file.readlines()
        raw_data_without_header = raw_data[1:] # remove header
        splitted = [row[:-1].split(';') for row in raw_data_without_header  if not row == ';;\n']
        postal_codes = [PostalCode(row[0], row[1], row[2]) for row in splitted]
        return postal_codes
