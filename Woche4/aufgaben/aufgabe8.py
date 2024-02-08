import json
def main():
    def own_parsing():
        #rows = json_file.readlines() # Das wird ein Irrweg!
        #print(rows)
        pass
    def using_string():
        with open ('Woche4/aufgaben/people.json') as json_file:
            text = json_file.read()
            data = json.loads(text)
            #print(data)
            print(data[0]["firstname"])
    def compact():
        with open ('Woche4/aufgaben/people.json') as json_file:
            data = json.load(json_file)
            print(data[0]["lastname"])

    using_string()
    compact()
main()