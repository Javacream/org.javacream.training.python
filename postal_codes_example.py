def postal_code_to_city():
    dict = {81373: "München", 33033: "Berlin"}
    print(dict.get(81373))
    print(dict.get(81374)) # hier würde dict[81374] mit einem Fehler aussteigen, get ist also etwas sanfter
    dict[40001] = "Hamburg"
    print(dict.get(40001))
    #dict.clear()
    #print(dict.get(40001))


def city_to_postal_codes():
    dict = {"München": [81373, 81333, 81555], "Berlin": [30333 ]}
    print(dict.get("München"))
    dict["Hamburg"] = [40001, 40444, 40888]
    print(dict.get("Hamburg"))
    print(dict.get("Hamburg")[1])


def main():
    postal_code_to_city()
    city_to_postal_codes()


main()