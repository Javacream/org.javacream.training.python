def number_of_rows_in(filename:str):
    with open (filename) as file:
        return len(file.readlines())
    
def main():
    filename = 'README.md'
    print(number_of_rows_in(filename))    

main()