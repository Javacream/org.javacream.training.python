import people
def main():
    id = input("Bitte geben Sie eine ID ein: ")
    id = int(id)
    result = people.find_by_id(id)
    print(result)

main()