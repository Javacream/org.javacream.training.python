import json

def main():

    with open ('./data/people.json', 'rt', encoding='utf-8') as file:
        data = json.load(file)
        print('done')

    data2 = [{"this": "that", "foo": "goo"}, {"this": "that2", "foo": "goo2"}]
    data2.append({'Hugo': 'Emil'})
    with open('result/demo.json', 'wt', encoding='utf-8') as file:
        json.dump(data2, file)
main()