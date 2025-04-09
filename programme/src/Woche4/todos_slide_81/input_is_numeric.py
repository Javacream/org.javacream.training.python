def get_data():
    with open ('programme/src/Woche4/input.txt', 'rt', encoding='utf-8') as input_file:
        data = input_file.read()
        if (data.endswith('\n')):
            data = data[:-1]
    return data
def check_data_is_numeric(data):
    if data.isnumeric():
        return f'{data} kann als Zahl interpretiert werden'
    else:
        return f'{data} kann nicht als Zahl interpretiert werden'
def write_result(result):
    with open ('programme/src/Woche4/output.txt', 'wt', encoding='utf-8') as output_file:
        output_file.write(f'{result}\n')
def main():
    data = get_data()
    result = check_data_is_numeric(data)
    write_result(result)
main()