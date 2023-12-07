def main():

    def read(source):
        print("step1: read data")
        with open(source, 'r', encoding='utf8') as pc_file:
            raw_data = pc_file.readlines()
        return raw_data
    
    def prepare(raw_data):
        print("step2: prepare data")
        federal_states = {}
        raw_data_without_header = raw_data[1:]
        for row in raw_data_without_header:
            row = row[0:len(row)-1] # remove \n
            data = row.split(',')
            federal_state = data[5]
            district = data[4]
            district_for_federal_state  = federal_states.get(federal_state)
            if district_for_federal_state == None:
                district_for_federal_state = set()
                federal_states[federal_state] = district_for_federal_state
            if (district == ""):
                district_for_federal_state.add('<Kreisfrei> \n')        
            else:
                if district.startswith('Landkreis'):
                    district = district[10:] # [10:] remove Landkreis
                district_for_federal_state.add(district + '\n')
        return federal_states
    
    def analyse(data):
        print("step3: analyse data")
        districts_of_bavaria = list(data.get("Bayern"))
        districts_of_bavaria.sort()
        return districts_of_bavaria
    def write(result, target):
        print("step4: write result")
        with open(target, 'w', encoding='utf8') as outfile:
            outfile.writelines(result)

    raw_data = read('zuordnung_plz_ort.csv')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, 'districts_of_bavaria.txt')

main()