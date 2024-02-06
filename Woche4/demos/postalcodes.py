def main():
    def read_data():
        with open("Woche4/demos/postalcodes.txt") as file:
            rows = file.readlines()
            postalcodes = dict()
            for row in rows:
                row = row.replace("\n", "")
                key_value = row.split(":")
                postalcodes[key_value[0]] = key_value[1]
            return postalcodes
    def query(postalcodes):
        while True:
            user_input = input("Bitte PLZ eingegeben, 'x' für Programmende: ")
            if user_input == 'x':
                break
            else:
                city = postalcodes.get(user_input)
                print(f"Stadt für PLZ {user_input} ist {city}")


    postalcode_dictionary = read_data()
    query(postalcode_dictionary)

main()