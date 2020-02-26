customers = { 1: "Cleese", 2:"Jones", 3: "Gilliam"}
addresses = { "Cleese": "London", "Jones": "Heaven"}


def get_address(customer_name):
    address = addresses.get(customer_name)
    if address == None:
        raise Exception("Unknown address for customer name " + customer_name)
    return address


def find_customer(customer_id):
    customer = customers.get(customer_id) 
    if customer == None:
        raise Exception("Unknown customer with id " + str(customer_id))
    return customer

