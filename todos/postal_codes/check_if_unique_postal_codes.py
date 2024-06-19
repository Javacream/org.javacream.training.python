import PostalCode as pc
def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    postal_codes = list()
    unique_postal_codes = set()
    for postal_code in data:
        postal_codes.append(postal_code.postal_code)
        unique_postal_codes.add(postal_code.postal_code)
    return len(postal_codes) == len(unique_postal_codes)

def write_result(result):
    #print(f"writing result: '{result}'")
    print(f"do we have duplicates: {result}")

def main():
    data = pc.read_data()
    result = pipeline(data)
    write_result(result)
main()