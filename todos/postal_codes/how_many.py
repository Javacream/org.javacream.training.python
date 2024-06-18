def read_data():
    print("reading data")
    with open ('german-postcodes.csv', 'r', encoding='utf-8') as file:
        return file.readlines()

def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    return len(data - 1) # header!

def write_result(result):
    print(f"writing result: '{result}'")
    print(f"we have {result} postal codes")
def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()