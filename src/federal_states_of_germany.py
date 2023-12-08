def main():

    def read(source):
        print("step1: read data")
        with open(source, 'r', encoding='utf8') as pc_file:
            raw_data = pc_file.readlines()
        return raw_data
    
    def prepare(raw_data):
        raw_data_without_header = raw_data[1:]
        federal_states = list()
        for row in raw_data_without_header:
            row = row[0:len(row)-1] # remove \n
            data = row.split(',')
            federal_state = data[5]
            federal_states.append(federal_state)
        return federal_states


    def analyse(data):
        federal_states_set = set()
        for federal_state in data:
            federal_states_set.add(federal_state + '\n')
        return federal_states_set

    def write(result, target):
        print("step4: write result")
        with open(target, 'w', encoding='utf8') as outfile:
            outfile.writelines(result)

    raw_data = read('zuordnung_plz_ort.csv')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, 'federal_states.txt')

main()