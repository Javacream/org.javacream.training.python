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
            athlets = int(data[4])
            teams = int(data[5])
            if games.get(year) == None:
                games[year] = athlets, teams 
        return games

    def analyse(data):
        print("step3: analyse data")
        result = list()
        for year, games_data in data.items():
            result.append(f'{year} {games_data[0]} {games_data[1]}\n')
        return result
   
    raw_data = read('olympic_games.csv')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, 'athlets_teams_per_game_rs.txt')
 
main()