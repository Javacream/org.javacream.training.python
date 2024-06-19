import PostalCode as pc
def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    postal_codes = dict()
    for postal_code in data:
        postal_codes[postal_code.postal_code] = postal_code.city
    return postal_codes

def write_result(result):
    #print(f"writing result: '{result}'")
    postal_code = input("Enter a 5-digit Postal Code: ")
    print(f"city for postal code {postal_code} is {result[postal_code]}")

def main():
    data = pc.read_data()
    result = pipeline(data)
    write_result(result)
main()