import people
import json
def main():
    result = people.find_all()
    with open ("people.json", "wt") as file:
        file.write(json.dumps(result))

main()