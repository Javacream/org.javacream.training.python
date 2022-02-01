from ordering import order
from shipping import ship

articel = "blueray"
number = 2
customer = 1
provider = "CGK"
try:
    order_id = order(articel, number, customer)
    confirmation = ship(order_id, provider)
    print(confirmation)
except Exception as e:
    print("Oops, something went wrong: ", e)
    

