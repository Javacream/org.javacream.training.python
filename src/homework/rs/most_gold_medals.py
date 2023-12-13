def main():
    def read(source):
        print("step1: read data")
        with open(source, 'r', encoding='utf8') as pc_file:
            raw_data = pc_file.readlines()
        return raw_data
    def write(result, target):
        print("step4: write result")
        with open(target, 'w', encoding='utf8') as outfile:
            outfile.writelines(result)
   
    def prepare(raw_data):
        print("step2: prepare data")
        games = dict()
        raw_data_without_header = raw_data[1:]
        for row in raw_data_without_header:
            row = row.replace('\n', '')
            data = row.split(',')
            year = int(data[0])
            country = data[7]
            gold = int(data[8])
            gold_list = games.get(year)
            if gold_list == None:
                gold_list = []
                games[year] = gold_list
            gold_list.append((country, gold)) 
        return games

    def analyse(data):
        result = []
        for year, gold_list in data.items():
            gold_list.sort(key = lambda tup: tup[1], reverse = True)
            max_gold = gold_list[0][1]
            index = 0
            while gold_list[index][1] == max_gold:
                result.append(f'{year} {gold_list[index][0]} {max_gold}\n')
                index += 1
        return result        
   
    raw_data = read('olympic_games.csv')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, 'most_gold_medals_rs.txt')

main()