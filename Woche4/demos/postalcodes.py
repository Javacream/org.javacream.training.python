def main():
    def read_data():
        with open(filename) as file:
            rows = file.readlines()
            for row in rows:
                row = row.replace("\n", "")
                key_value = row.split(":")
                postalcode_dictionary[key_value[0]] = key_value[1]
    def query():
        while True:
            user_input = input("Bitte PLZ eingegeben, 'x' für Programmende: ")
            if user_input == 'x':
                break
            else:
                city = postalcode_dictionary.get(user_input)
                print(f"Stadt für PLZ {user_input} ist {city}")


    filename = "Woche4/demos/postalcodes.txt"
    postalcode_dictionary = dict()
    read_data()
    query()

main()