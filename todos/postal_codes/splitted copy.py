def read_data():
    print("reading data")
    with open ('german-postcodes.csv', 'r') as file:
        return file.readlines()

def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    data_without_header = data[1:] # remove header
    result = [row.split(';') for row in data_without_header]
    return result

def write_result(result):
    #print(f"writing result: '{result}'")
    print(f"first splitted row: {result[0]}, city={result[0][0]}, plz={result[0][1]}, district={result[0][2]}")
def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()