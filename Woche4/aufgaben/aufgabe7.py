def main():
    def number_of_rows_in_file(filename):
        with open (f"Woche4/aufgaben/{filename}") as file:
            return len(file.readlines())
    print(number_of_rows_in_file(input("datei im aufgaben-Ordner: ")))
main()