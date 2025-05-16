import mysql.connector

def read_shopping_list():
    HOST = 'javacream.eu'
    PORT = 3406
    DATABASE_NAME = 'javacream'
    USER = 'user'
    PWD = 'user'

    connection = mysql.connector.connect(
        host=HOST, 
        port = PORT,
        database = DATABASE_NAME,
        user = USER,
        password = PWD
        )
    cursor = connection.cursor()
    sql_statement = "select * from SHOPPING_LIST"
    cursor.execute(sql_statement)
    result = cursor.fetchall()
    connection.commit() # Das dient zum endgültigen Bestätigen des Schreibevorgangs
    rows = [f'{data[0]} {data[1]} {str(data[2])}' for data in result]
    return rows

def create_shopping_data(data_list):
    shopping_data = [(data.split(" ")[0], data.split(" ")[1], int(data.split(" ")[2])) for data in data_list]
    return shopping_data

def write_shopping_data(shopping_data):
    print(shopping_data)

def create_unique_names(shopping_data):
    uniques = {data[0] for data in shopping_data}
    return uniques

def create_unique_products(shopping_data):
    uniques = {data[1] for data in shopping_data}
    return uniques

def create_products_amounts(shopping_data):
    products = create_unique_products(shopping_data)
    products_amount = dict()
    for product in products:
        products_amount[product] = 0
    for data in shopping_data:
        product = data[1]
        amount = data[2]
        old_amount = products_amount[product]
        products_amount[product] = old_amount + amount
    return products_amount

def create_products_by_people(shopping_data):
    people = create_unique_names(shopping_data)
    products_by_people = {person : set() for person in people}
    for data in shopping_data:
        products_by_people[data[0]].add(data[1])
    return products_by_people    
