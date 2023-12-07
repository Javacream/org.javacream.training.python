def main():

    def read(source):
        print("step1: read data")
        return {} # or list
    def prepare(raw_data):
        print("step2: prepare data")
        return {}
    def analyse(data):
        print("step3: analyse data")
        return 'result'
    def write(result, target):
        print("step4: write result")

    raw_data = read('')
    data = prepare(raw_data)
    result = analyse(data)
    write(result, '')

main()