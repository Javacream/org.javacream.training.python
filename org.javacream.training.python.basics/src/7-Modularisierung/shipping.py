from ordering import find_order
from customer import get_address

providers = {"EIM": 5.99, "CGK": 3.99}
 
def ship(order_id, provider):
    order = find_order(order_id) 
    customer_address = get_address(order["customer"])
    shipping =  calculate_shipping(provider)
    total_price = order["total"]
    order["total"] = total_price + shipping
    return {"order": order, "address": customer_address}

def calculate_shipping (provider):
    shipping = providers.get(provider)
    if shipping == None:
        shipping = 9.99
    return shipping 
