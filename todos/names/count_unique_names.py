def read_data():
    print("reading data")
    with open('./names.txt') as file:
        return file.readlines()

def pipeline(data):
    print(f"executing pipeline with data '{data}'")
    unique_names = set(data)
    result = len(unique_names)
    return result

def write_result(result):
    print(f"writing result: '{result}'")
    print(f"number of unique names in names.txt: {result}")
def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()