prices = {"blueray": 5.99, "cd": 9.99, "dvd": 14.99}
discounts = {"blueray": 0, "cd": 30, "dvd": 10}

def calculate_price(articel):
    price = prices.get(articel)
    discount = discounts.get(articel)
    discounted_price = price * (1 - discount/100)
    return price

def total_price(price, number):
    return price * number

