def get_data():
    data = input("Bitte etwas eingeben: ")
    return data
def check_data_is_numeric(data):
    if data.isnumeric():
        return f'{data} kann als Zahl interpretiert werden'
    else:
        return f'{data} kann nicht als Zahl interpretiert werden'

def main():
    data = get_data()
    result = check_data_is_numeric(data)
    print(result)
main()