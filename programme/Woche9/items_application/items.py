import mysql.connector
import random
class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    def __repr__(self):
        return f'Item: id={self.id}, name={self.name}, price={self.price}'

class ItemService:

    def __init__(self):
        self.database = mysql.connector.connect(
        host = "javacream.eu",
        port = 3406,
        database = 'javacream',
        user = 'user',
        password = 'user'
        )
    def create(self, name, price):
        id = random.randint(0, 1000000)
        cursor = self.database.cursor()
        cursor.execute(f"INSERT INTO ITEMS (id, name, price) VALUES ({id}, '{name}', {price})")
        self.database.commit()
        cursor.close()
        return id
    def find_by_id(self, id):
        cursor = self.database.cursor()
        cursor.execute(f"SELECT * FROM ITEMS WHERE id = {id}")
        result = cursor.fetchall()
        if (len(result) == 1):
            row = result[0]
            return Item(row[0], row[1], row[2])
        else:
            return None
    def find_by_name(self, name):
        cursor = self.database.cursor()
        cursor.execute(f"SELECT * FROM ITEMS WHERE name = '{name}'")
        result = cursor.fetchall()
        return [Item(row[0], row[1], row[2]) for row in result]