from ordering import order
from shipping import ship


def main():
    articel = "cd"
    number = 2
    customer = 1
    provider = "CGK"

    order_id = order(articel, number, customer)
    confirmation = ship(order_id, provider)
    print(confirmation)

if __name__ == "__main__":
    main()