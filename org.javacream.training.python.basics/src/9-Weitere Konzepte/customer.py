customers = { 1: "Meier", 2:"Metzger", 3: "Mustermann"}
addresses = { "Meier": "München Marienplatz", "Metzger": "Berlin Alexanderplatz"}


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

