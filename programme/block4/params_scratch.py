def print_out(data_dict):
    for key in data_dict:
        print(f'{key}={data_dict[key]}')

def print_out2(**data_dict):
    for key in data_dict:
        print(f'{key}={data_dict[key]}')

def main():
    data = {'name': 'Sawitzki', 'height': 183}
    print_out(data)
    print_out2(name='Sawitzki', height=183)
main()