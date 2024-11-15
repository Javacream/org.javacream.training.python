import requests

def main():
    url = 'http://javacream.eu:8080/api/books'
    response = requests.get(url)
    if response.status_code == 200:
        book_datas = response.json()
        for book_data in book_datas:
            print(book_data['title'])
    else:
        print(f'Error, status={response.status_code}')

if __name__ == '__main__':
    main()