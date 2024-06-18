def read_data():
    print("reading data")
    with open ('german-postcodes.csv', 'r', encoding='utf-8') as file:
        return file.readlines()

def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    data_without_header = data[1:] # remove header
    splitted = [row.split(';') for row in data_without_header]
    postal_codes = dict()
    for splitted_row in splitted:
        postal_codes[splitted_row[1]] = splitted_row[0]
    return postal_codes

def write_result(result):
    #print(f"writing result: '{result}'")
    postal_code = input("Enter a 5-digit Postal Code: ")
    print(f"city for postal code {postal_code} is {result[postal_code]}")

def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()