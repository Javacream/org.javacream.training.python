base_path = './programme/demos/block3'
while True:
    file_name = input ('Name der Datei: ')
    path = f'{base_path}/{file_name}'
    try:
        with open (path, 'rt') as file:
            rows = file.readlines()
        for row in rows:
            if (row[-1] == '\n'):
                print(row[:-1])
            else:
                print(row)    
    except Exception as e:
        print(f'falscher Dateiname: {file_name}: {e}')    
    again = input ('Nochmal ? j|n')
    if again == 'n':
        break    