import PostalCode as pc
def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    cities_of_bavaria = [postal_code.city for postal_code in data if postal_code.district == "Bayern"]
    return cities_of_bavaria
def write_result(result):
    #print(f"writing result: '{result}'")
    print(f"cities of bavaria: {result}")

def main():
    data = pc.read_data()
    result = pipeline(data)
    write_result(result)
main()