import requests
def main():
    json_response = requests.get('https://jsonplaceholder.typicode.com/users').json()
    for user_dict in json_response:
        print(f'User: id={user_dict["id"]}, name={user_dict["name"]}')

main()  