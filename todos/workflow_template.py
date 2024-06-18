def read_data():
    print("reading data")
    return "template data"

def pipeline(data):
    print(f"executing pipeline with data '{data}'")
    return "result data"

def write_result(result):
    print(f"writing result: '{result}'")

def main():
    data = read_data()
    result = pipeline(data)
    write_result(result)
main()