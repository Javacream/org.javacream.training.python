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
        return {}

    def analyse(data):
        print("step3: analyse data")
        return 'result'
    
    raw_data = read('olympic_games.csv')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, 'olympics_analysis_result.txt')

main()