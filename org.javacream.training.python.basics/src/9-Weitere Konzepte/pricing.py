prices = {"blueray": 5.99, "cd": 9.99, "dvd": 14.99}
discounts = {"cd": 30, "dvd": 10}

def calculate_price(articel):
    price = prices.get(articel)
    if price == None:
        raise Exception("Unknown article " + articel)
    discount = discounts.get(articel)
    if discount == None:
        discount = 0
    discounted_price = price * (1 - discount/100)
    return price

def total_price(price, number):
    return price * number

