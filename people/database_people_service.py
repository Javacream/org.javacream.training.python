import mysql.connector

class PeopleService:
    def __init__(self, config):
        self.config = config

    def read_people(self):
        try:
            with mysql.connector.connect(**self.config) as connection:
                cursor = connection.cursor()
                cursor.execute(f'SELECT * FROM PEOPLE')
                data = cursor.fetchall()
                people = [Person(element[0], element[2], element[1], float(element[3]), element[5]) for element in data]
                return people
                #return data
        except Exception as e:
            print(e)

class Person:
    def __init__(self, id, lastname, firstname, height, gender):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.gender = gender
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.id == other.id
        else:
            return False
    def __hash__(self):
        return self.id
    def __repr__(self):
        return f'Person(id={self.id}, lastname={self.lastname}, firstname={self.firstname}, gender={self.gender}, height={self.height})'