# class PostalCode:
#     def __init__(self, city, postal_code, district):
#         self.city = city
#         self.postal_code = postal_code
#         self.district = district
#     def __repr__(self):
#         return f"PostalCode: city=..."    
import PostalCode as pc
def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    cities = dict()
    for postal_code in data:
        postal_codes = cities.get(postal_code.city)
        if postal_codes == None:
            postal_codes = []
            cities[postal_code.city] = postal_codes

        postal_codes.append(postal_code.postal_code) 
    return cities

def write_result(result):
    #print(f"writing result: '{result}'")
    city = input("Enter a city name: ")
    print(f"postal codes for city {city} are {result[city]}")

def main():
    data = pc.read_data()
    result = pipeline(data)
    write_result(result)
main()