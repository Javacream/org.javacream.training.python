from pricing import calculate_price
from pricing import total_price
from customer import find_customer

orders = []

def order(articel, number, customer_id):
    try:
        price = calculate_price(articel)
        total = total_price(price, number)
        customer_name = find_customer(customer_id)
        order = {"articel": articel, "total": total, "customer": customer_name}
        orders.append(order)
        return len(orders) - 1
    except Exception as e:
        raise
def find_order(id):
    return orders[id]
