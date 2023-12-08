with open('zuordnung_plz_ort.csv', 'r', encoding='utf8') as pc_file:
    raw_data = pc_file.readlines()
    raw_data_without_header = raw_data[1:]
    federal_states = set()
    for row in raw_data_without_header:
        row = row[0:len(row)-1] # remove \n
        data = row.split(',')
        federal_state = data[5]   
        federal_states.add(federal_state)
    print(str(federal_states))    
 
