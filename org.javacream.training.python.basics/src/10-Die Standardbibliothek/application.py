import traceback
import random
from ordering import order
from shipping import ship

articel = "blueray"
number = random.randint(1, 50)
customer = random.randint(1, 3)
provider = "CGK"
try:
    order_id = order(articel, number, customer)
    confirmation = ship(order_id, provider)
    print(confirmation)
except Exception as e:
    print("Oops, something went wrong: ", e)
    traceback.print_exc()

