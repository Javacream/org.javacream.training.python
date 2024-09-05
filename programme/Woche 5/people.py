class Person:
    def __init__(self, lastname:str, firstname:str, height:int):
        self.lastname = lastname
        self.firstname = firstname
        self.height = height
        self.__name = f'{self.firstname} {self.lastname}'
    def say_hello(self) -> str: 
        return f'Hello, my name is {self.__name}'    
