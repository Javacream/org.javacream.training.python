customers = { 1: "Meier", 2:"Metzger", 3: "Mustermann"}
addresses = { "Meier": "München Marienplatz", "Metzger": "Berlin Alexanderplatz", "Mustermann": "Stuttgart Königsplatz"}


def get_address(customer_name):
    return addresses.get(customer_name)


def find_customer(customer_id):
    return customers.get(customer_id)

