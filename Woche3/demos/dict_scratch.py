# Postleitzahlen und zugehörige Städte
def get_city_for_code_with_if(code):
    if code == "81371":
        return "München"
    elif code == "70567":
        return "Stuttgart"
    elif code == "40111":
        return "Hamburg"

def get_city_for_code(code):
    postal_codes = {"81371": "München", "70567": "Stuttgart", "40111": "Hamburg"}
    # city_result = postal_codes[code]
    city_result = postal_codes.get(code)
    return city_result

def main():
    postal_code1 = "81371"
    postal_code2 = "70567"

    city1 = get_city_for_code(postal_code1)
    city2 = get_city_for_code(postal_code2)
    print(f"{city1}, {city2}")
    print(get_city_for_code_with_if("60666"))
    print(get_city_for_code("60666"))

main()