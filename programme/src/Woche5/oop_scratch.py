def Person(name, weight, height):
    new_person = dict()
    new_person["name"] = name
    new_person["weight"] = weight
    new_person["height"] = height
    return new_person

def main():
    height = 183
    weight = 75.7
    name = "Sawitzki"

    person1_dict = {"name": "Sawitzki", "weight": 75.7, "height": 183}
    person2_dict = {"x": "Sawitzki", "y": 75.7, "z": 183}
    person1 = Person("Sawitzki", 183, 75.7)
    person2 = Person("Meier", 189, 83.5)

    print('done')
main()