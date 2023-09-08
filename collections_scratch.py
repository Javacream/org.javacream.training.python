def scratch_list_sort():
    names = ["Hugo", "Emil", "Fritz"]
    names.sort(reverse=False)
    print(names)

def scratch_basic_data_analysis():
    names = ["Hugo", "Emil", "Fritz", "Eduard"]
    # Filter-Logik: Nur Elemente, die mit dem Buchstaben "E" beginnen
    filtered_names = []
    for name in names:
        if name.startswith("E"):
            filtered_names.append(name)
    # Transformation: Umwandlung in Großbuchstaben
    transformed_names = []
    for name in filtered_names:
        transformed_names.append(name.upper())

    print(transformed_names)    

def scratch_basic_data_analysis_with_comprehensions():
    names = ["Hugo", "Emil", "Fritz", "Eduard"]
    # Pseudocode select name.upper() from names where name startswith 'E'
    # Umsetzung in Python Comprehension
    filtered_and_transformed_names = [name.upper() for name in names if name.startswith("E")]
    print(filtered_and_transformed_names)


scratch_basic_data_analysis_with_comprehensions()