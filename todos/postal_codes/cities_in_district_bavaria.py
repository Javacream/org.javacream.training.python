def read_data():
    print("reading data")
    with open ('german-postcodes.csv', 'r', encoding='utf-8') as file:
        return file.readlines()

def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    data_without_header = data[1:] # remove header
    splitted = [row.split(';') for row in data_without_header]
    cities_of_bavaria = [row[0] for row in splitted if row[2][:-1] == "Bayern"]
    return cities_of_bavaria
def write_result(result):
    #print(f"writing result: '{result}'")
    print(f"cities of bavaria: {result}")

def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()