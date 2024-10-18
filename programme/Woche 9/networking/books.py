import requests
from statistics import mean
ENDPOINT = 'http://javacream.eu:8080/api/books'

def read_all():
    return requests.get(ENDPOINT).json()
def min_price(books):
    return min([b['price'] for b in books])
def max_price(books):
    return max([b['price'] for b in books])
def avg_price(books):
    return mean([b['price'] for b in books])

def main():
    books = read_all()
    print(f'min price: {min_price(books)}')
    print(f'max price: {max_price(books)}')
    print(f'average price: {avg_price(books)}')
if __name__ == '__main__':
    main()