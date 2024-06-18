def read_data():
    print("reading data")
    with open('./names.txt') as file:
        return file.readlines()

def pipeline(data):
    print(f"executing pipeline with data '{data}'")
    result = len(data)
    return result

def write_result(result):
    print(f"writing result: '{result}'")
    print(f"number of names in names.txt: {result}")
def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()