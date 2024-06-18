def read_data():
    print("reading data")
    with open ('german-postcodes.csv', 'r', encoding='utf-8') as file:
        return file.readlines()

def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    data_without_header = data[1:] # remove header
    splitted = [row.split(';') for row in data_without_header]
    cities = dict()
    for splitted_row in splitted:
        city = splitted_row[0]
        postal_codes = cities.get(city)
        if postal_codes == None:
            postal_codes = []
            cities[city] = postal_codes

        postal_codes.append(splitted_row[1]) 
    return cities

def write_result(result):
    #print(f"writing result: '{result}'")
    city = input("Enter a city name: ")
    print(f"postal codes for city {city} are {result[city]}")

def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()