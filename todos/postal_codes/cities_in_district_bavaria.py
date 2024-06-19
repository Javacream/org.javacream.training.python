import PostalCode as pc
import csv
def pipeline(data):
    #print(f"executing pipeline with data '{data}'") # huge console output!
    cities_of_bavaria = [postal_code for postal_code in data if postal_code.district == "Bayern"]
    return cities_of_bavaria
def write_result(result):
    with open ('cities_of_bavaria.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=':')
        for row in result:
            writer.writerow([row.postal_code, row.city])
def main():
    data = pc.read_data()
    result = pipeline(data)
    write_result(result)
main()