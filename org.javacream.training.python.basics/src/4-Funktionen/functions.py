def calculate_price(original , discount_in_percent, shipping):
    discounted_price = original * (1 - discount_in_percent/100)
    price = discounted_price + shipping
    return price

def calculate_shipping (provider):
    if provider == "EIM":
        shipping = 5.99
    elif provider == "CGK":
        shipping = 3.99
    else:
        shipping = 9.99
    return shipping 

def order():
    provider = "EIM"
    shipping = calculate_shipping(provider)
    original_price = 19.99
    price = calculate_price(original_price, 10, shipping)
    print("total price: ", price)

percent_to_discount = lambda percent: (1 - percent/100)

order()    

def calculate_price_with_lambda(original , discount_in_percent, shipping):
    discounted_price = original * percent_to_discount(discount_in_percent)
    price = discounted_price + shipping
    return price
print(calculate_price_with_lambda(19.99, 10, 5.99))

