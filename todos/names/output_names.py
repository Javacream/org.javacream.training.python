def read_data():
    print("reading data")
    with open('./names.txt') as file:
        return file.readlines()

def pipeline(data):
    print(f"executing pipeline with data '{data}'")
    result = []
    for name in data:
        if name.endswith('\n'):
            result.append(name[:-1])
        else:
            result.append(name)    
    return result

def write_result(result):
    print(f"writing result: '{result}'")
    for name in result:
        print(name)

def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()