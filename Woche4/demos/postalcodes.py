def main():
    def read_data(**kwargs):
        with open(f"{kwargs['directory']}/{kwargs['filename']}") as file:
            postalcode_dictionary = dict()
            rows = file.readlines()
            for row in rows:
                row = row.replace("\n", "")
                key_value = row.split(":")
                postalcode_dictionary[key_value[0]] = key_value[1]
            return postalcode_dictionary    
    def query(postalcode_dictionary):
        while True:
            user_input = input("Bitte PLZ eingegeben, 'x' für Programmende: ")
            if user_input == 'x':
                break
            else:
                city = postalcode_dictionary.get(user_input)
                print(f"Stadt für PLZ {user_input} ist {city}")


    filename = "postalcodes.txt"
    dirname = "Woche4/demos"
    postalcode_dictionary = read_data(directory = dirname, filename = filename)
    query(postalcode_dictionary)

main()