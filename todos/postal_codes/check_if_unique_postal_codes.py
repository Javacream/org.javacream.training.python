def read_data():
    print("reading data")
    with open ('german-postcodes.csv', 'r', encoding='utf-8') as file:
        return file.readlines()

def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    data_without_header = data[1:] # remove header
    splitted = [row.split(';') for row in data_without_header]
    postal_codes = list()
    unique_postal_codes = set()
    for splitted_row in splitted:
        postal_codes.append(splitted_row[1])
        unique_postal_codes.add(splitted_row[1])
    return len(postal_codes) == len(unique_postal_codes)

def write_result(result):
    #print(f"writing result: '{result}'")
    print(f"do we have duplicates: {result}")

def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()