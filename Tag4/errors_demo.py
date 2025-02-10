
def main():
    while True:
        input_string = input('Nummer angeben: ')
        if input_string == 'x':
            break
        try:
            input_string = int(input_string)
            print(input_string * 2)
        except:
            print(f'{input_string} war keine Zahl ')    
if __name__ == '__main__':
    main()