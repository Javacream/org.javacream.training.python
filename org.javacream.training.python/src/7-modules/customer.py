customers = { 1: "Cleese", 2:"Jones", 3: "Gilliam"}
addresses = { "Cleese": "London", "Jones": "Heaven"}


def get_address(customer_name):
    return addresses.get(customer_name)


def find_customer(customer_id):
    return customers.get(customer_id)

