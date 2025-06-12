def fn(**params_dict):
    print(params_dict)
    for key in params_dict:
        print(f'{key} -> {params_dict[key]}')

def main():
    fn()
    fn(this='that')
    fn(eg='al', auch='egal')


main()