from ordering import order
from shipping import ship

articel = "cd"
number = 2
customer = 1
provider = "CGK"

order_id = order(articel, number, customer)
confirmation = ship(order_id, provider)
print(confirmation)

