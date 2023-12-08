def main():
    def read(source):
        print("step1: read data")
        with open(source, 'r', encoding='utf8') as pc_file:
            raw_data = pc_file.readlines()
        return raw_data
    
    def write(result, target):
        print("step4: write result")
        with open(target, 'w', encoding='utf8') as outfile:
            outfile.writelines([f"{e[0]} = {e[1]}\n" for e in result])
    
    def prepare(raw_data):
        print("step2: prepare data")
        games = dict()
        raw_data_without_header = raw_data[1:]
        for row in raw_data_without_header:
            row = row.replace('\n', '')
            data = row.split(',')
            year = int(data[0])
            country = data[7]
            bronze_count = int(data[10])
            bronze_per_year = games.get(country)
            if bronze_per_year == None:
                bronze_per_year = []
                games[country] = bronze_per_year
            data_tuple = (year, bronze_count)
            bronze_per_year.append(data_tuple)
        return games

    def analyse(data):
        print("step3: analyse data")
        result = list()
        for country, infos in data.items():
            bronzemedal_count = 0
            for info in infos:
                bronzemedal_count = bronzemedal_count + info[1]
            result.append((country, bronzemedal_count))
        return result
    
    raw_data = read('olympic_games.csv')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, 'olympics_analysis_result.txt')

main()