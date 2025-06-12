import json

def main():

    with open ('./data/people.json', 'rt', encoding='utf-8') as file:
        data = json.load(file)
        print('done')

main()